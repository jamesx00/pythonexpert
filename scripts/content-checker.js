// Verifies every exercise lesson in every course: front matter parses, the
// files it references exist, the reference solution passes every test, the
// starter fails at least one, and the listed test IDs match the test file.
const fs = require("fs");
const os = require("os");
const path = require("path");
const { execFile } = require("child_process");
const yaml = require("js-yaml");

const DEFAULT_TIMEOUT_MS = 20000;

function listLessonDirs(coursesDir) {
	const lessons = [];
	for (const course of fs.readdirSync(coursesDir, { withFileTypes: true })) {
		if (!course.isDirectory()) continue;
		const courseDir = path.join(coursesDir, course.name);
		for (const lesson of fs.readdirSync(courseDir, { withFileTypes: true })) {
			if (!lesson.isDirectory() || lesson.name === "files") continue;
			const lessonDir = path.join(courseDir, lesson.name);
			if (fs.existsSync(path.join(lessonDir, "index.md"))) {
				lessons.push({ name: `${course.name}/${lesson.name}`, dir: lessonDir });
			}
		}
	}
	return lessons.sort((a, b) => a.name.localeCompare(b.name));
}

function parseLesson(markdown) {
	const match = markdown.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
	if (!match) throw new Error("missing front matter");
	const data = yaml.load(match[1]);
	if (data === null || typeof data !== "object" || Array.isArray(data)) {
		throw new Error("front matter is not a mapping");
	}
	return { data, body: match[2] };
}

// A lesson's file may live in its own files/ folder or the course's shared one.
function resolveSource(lessonDir, source) {
	const candidates = [
		path.join(lessonDir, "files", source),
		path.join(lessonDir, "..", "files", source),
	];
	return candidates.find((candidate) => fs.existsSync(candidate)) || null;
}

function listedTestIds(body) {
	const ids = new Set();
	for (const match of body.matchAll(/id="test-(\d+)"/g)) {
		ids.add(Number(match[1]));
	}
	return ids;
}

function runPython(python, cwd, script, timeoutMs) {
	return new Promise((resolve) => {
		execFile(
			python,
			[script],
			{ cwd, timeout: timeoutMs, maxBuffer: 64 * 1024 * 1024 },
			(error, stdout, stderr) => {
				resolve({
					stdout,
					stderr,
					timedOut: Boolean(error && error.killed),
				});
			}
		);
	});
}

// Mirrors the front-end: stdout is either one JSON object of test ID → result,
// or anything else (the raw-output fallback).
function parseResults(stdout) {
	let parsed;
	try {
		parsed = JSON.parse(stdout);
	} catch (e) {
		return null;
	}
	if (parsed === null || typeof parsed !== "object" || Array.isArray(parsed)) {
		return null;
	}
	return parsed;
}

function isPassed(value) {
	if (value === true) return true;
	return value !== null && typeof value === "object" && value.passed === true;
}

async function runExercise({ group, commonGroups, lessonDir, mainFile, replacement, python, timeoutMs }) {
	const workDir = fs.mkdtempSync(path.join(os.tmpdir(), "content-check-"));
	try {
		for (const file of [...commonGroups.flatMap((g) => g.files), ...group.files]) {
			const source =
				file === mainFile && replacement
					? replacement
					: resolveSource(lessonDir, file.source);
			fs.copyFileSync(source, path.join(workDir, file.file_name));
		}
		const testFile = group.files.find((file) => file.is_test_file);
		return await runPython(python, workDir, testFile.file_name, timeoutMs);
	} finally {
		fs.rmSync(workDir, { recursive: true, force: true });
	}
}

// The learner's file: the one the editor focuses, falling back to the main file.
function findMainFile(group) {
	return (
		group.files.find((file) => file.is_edit_focus && file.is_editable) ||
		group.files.find((file) => file.is_main)
	);
}

async function checkLesson(lesson, options) {
	const errors = [];
	const fail = (message, testId) =>
		errors.push(
			testId === undefined
				? { lesson: lesson.name, message }
				: { lesson: lesson.name, testId, message }
		);

	let parsed;
	try {
		parsed = parseLesson(fs.readFileSync(path.join(lesson.dir, "index.md"), "utf-8"));
	} catch (e) {
		fail(`invalid front matter: ${e.message.split("\n")[0]}`);
		return errors;
	}
	const { data, body } = parsed;

	const fileGroups = data.file_groups || [];
	for (const group of fileGroups) {
		for (const file of group.files || []) {
			if (!resolveSource(lesson.dir, file.source)) {
				fail(`file "${file.source}" referenced in front matter does not exist`);
			}
		}
	}
	if (errors.length > 0) return errors;

	const commonGroups = fileGroups.filter((group) => group.common);
	const exerciseGroups = fileGroups.filter(
		(group) =>
			!group.common &&
			(group.files || []).some(
				(file) => file.is_test_file && file.file_type === "python"
			)
	);

	for (const group of exerciseGroups) {
		const mainFile = findMainFile(group);
		const run = (replacement) =>
			runExercise({
				group,
				commonGroups,
				lessonDir: lesson.dir,
				mainFile,
				replacement,
				python: options.python,
				timeoutMs: options.timeoutMs,
			});

		const listed = listedTestIds(body);

		const starterRun = await run(null);
		if (starterRun.timedOut) {
			fail("starter code run timed out");
			continue;
		}

		const extension = path.extname(mainFile.file_name);
		const reference = path.join(lesson.dir, "files", `solution${extension}`);
		if (!fs.existsSync(reference)) continue;

		const starterResults = parseResults(starterRun.stdout);
		if (
			starterResults !== null &&
			[...listed].every((id) => isPassed(starterResults[id]))
		) {
			fail("starter code passes every test; at least one should fail");
		}

		const referenceRun = await run(reference);
		const referenceResults = parseResults(referenceRun.stdout);
		if (referenceRun.timedOut) {
			fail("reference solution run timed out");
			continue;
		}
		if (referenceResults === null) {
			fail(`reference solution run did not print a JSON result: ${summarize(referenceRun)}`);
			continue;
		}
		const reported = new Set(Object.keys(referenceResults).map(Number));
		const allIds = [...new Set([...listed, ...reported])].sort((a, b) => a - b);
		for (const id of allIds) {
			if (!listed.has(id)) {
				fail("test file reports this test ID but the lesson does not list it", id);
			} else if (!reported.has(id)) {
				fail("lesson lists this test ID but the test file does not report it", id);
			} else if (!isPassed(referenceResults[id])) {
				fail("reference solution fails this test", id);
			}
		}
	}

	return errors;
}

function summarize(run) {
	const text = (run.stderr || run.stdout || "no output").trim();
	return text.split("\n").slice(-1)[0].slice(0, 300);
}

async function mapWithConcurrency(items, limit, fn) {
	const results = new Array(items.length);
	let next = 0;
	const workers = Array.from({ length: Math.min(limit, items.length) }, async () => {
		while (next < items.length) {
			const index = next++;
			results[index] = await fn(items[index]);
		}
	});
	await Promise.all(workers);
	return results;
}

async function checkCourses(coursesDir, options = {}) {
	const resolved = {
		python: options.python || process.env.PYTHON || "python3",
		timeoutMs: options.timeoutMs || DEFAULT_TIMEOUT_MS,
	};
	const lessons = listLessonDirs(coursesDir);
	const perLesson = await mapWithConcurrency(
		lessons,
		options.concurrency || os.cpus().length,
		(lesson) => checkLesson(lesson, resolved)
	);
	return { errors: perLesson.flat(), lessonsChecked: lessons.length };
}

module.exports = { checkCourses };
