// Verifies every exercise lesson in every course: front matter parses, the
// files it references exist, the reference solution passes every test, the
// starter fails at least one, and the listed test IDs match the test file.
const fs = require("fs");
const os = require("os");
const path = require("path");
const { execFile } = require("child_process");
const yaml = require("js-yaml");
const { parseTestOutput, toTestState } = require("../public/js/test-results");

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

const DIFFICULTIES = ["easy", "medium", "hard"];

const isNonEmptyString = (value) =>
	typeof value === "string" && value.trim() !== "";

// Optional lesson metadata; see the content contribution guide for the format.
function metadataErrors(data) {
	const errors = [];
	if (data.difficulty !== undefined && !DIFFICULTIES.includes(data.difficulty)) {
		errors.push(
			`difficulty must be one of ${DIFFICULTIES.join(", ")} (got ${JSON.stringify(data.difficulty)})`
		);
	}
	const complexity = data.target_complexity;
	if (complexity !== undefined) {
		if (complexity === null || typeof complexity !== "object") {
			errors.push("target_complexity must have a time (and optionally a space) field");
		} else {
			if (!isNonEmptyString(complexity.time)) {
				errors.push("target_complexity.time must be a non-empty string");
			}
			if (complexity.space !== undefined && !isNonEmptyString(complexity.space)) {
				errors.push("target_complexity.space must be a non-empty string");
			}
		}
	}
	if (
		data.hints !== undefined &&
		!(Array.isArray(data.hints) && data.hints.every(isNonEmptyString))
	) {
		errors.push("hints must be a list of non-empty strings");
	}
	if (data.checkpoint === true && data.hints !== undefined) {
		errors.push("checkpoint lessons must not have hints");
	}
	for (const flag of ["checkpoint", "rich_test_results"]) {
		if (data[flag] !== undefined && typeof data[flag] !== "boolean") {
			errors.push(`${flag} must be true or false`);
		}
	}
	return errors;
}

// A lesson's file may live in its own files/ folder or the course's shared one.
function resolveSource(lessonDir, source) {
	const candidates = [
		path.join(lessonDir, "files", source),
		path.join(lessonDir, "..", "files", source),
	];
	return candidates.find((candidate) => fs.existsSync(candidate)) || null;
}

// The lesson layout embeds each shipped file with btoa, which throws on any
// character above U+00FF, and the build then fails with a misleading ENOENT.
function nonLatin1Char(text) {
	const lines = text.split("\n");
	for (let i = 0; i < lines.length; i++) {
		for (const char of lines[i]) {
			const code = char.codePointAt(0);
			if (code > 0xff) {
				const hex = code.toString(16).toUpperCase().padStart(4, "0");
				return { line: i + 1, char, codePoint: `U+${hex}` };
			}
		}
	}
	return null;
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

const isPassed = (results, id) =>
	results[id] !== undefined && toTestState(id, results[id]).status === "passed";

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

	for (const message of metadataErrors(data)) {
		fail(message);
	}

	const fileGroups = data.file_groups || [];
	for (const group of fileGroups) {
		for (const file of group.files || []) {
			const source = resolveSource(lesson.dir, file.source);
			if (!source) {
				fail(`file "${file.source}" referenced in front matter does not exist`);
				continue;
			}
			const problem = nonLatin1Char(fs.readFileSync(source, "utf-8"));
			if (problem) {
				fail(
					`file "${file.source}" line ${problem.line} contains "${problem.char}" (${problem.codePoint}), ` +
						"which the site can't embed (btoa only accepts Latin-1); use an escape such as \\u2192 instead"
				);
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

		const listedIds = listedTestIds(body);

		const starterRun = await run(null);
		if (starterRun.timedOut) {
			fail("starter code run timed out");
			continue;
		}
		const starter = parseTestOutput(starterRun.stdout);
		if (!starter.isJson && starterRun.stderr !== "") {
			fail(`starter run crashed without printing a JSON result: ${summarize(starterRun)}`);
			continue;
		}

		const extension = path.extname(mainFile.file_name);
		const reference = path.join(lesson.dir, "files", `solution${extension}`);
		if (!fs.existsSync(reference)) continue;

		if (
			starter.isJson &&
			listedIds.size > 0 &&
			[...listedIds].every((id) => isPassed(starter.results, id))
		) {
			fail("starter code passes every test; at least one should fail");
		}

		const referenceRun = await run(reference);
		if (referenceRun.timedOut) {
			fail("reference solution run timed out");
			continue;
		}
		const referenceOutput = parseTestOutput(referenceRun.stdout);
		if (!referenceOutput.isJson) {
			fail(`reference solution run did not print a JSON result: ${summarize(referenceRun)}`);
			continue;
		}
		const referenceResults = referenceOutput.results;
		const reportedIds = new Set(Object.keys(referenceResults).map(Number));
		const allIds = [...new Set([...listedIds, ...reportedIds])].sort((a, b) => a - b);
		for (const id of allIds) {
			if (!listedIds.has(id)) {
				fail("test file reports this test ID but the lesson does not list it", id);
			} else if (!reportedIds.has(id)) {
				fail("lesson lists this test ID but the test file does not report it", id);
			} else if (!isPassed(referenceResults, id)) {
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
	const runOptions = {
		python: options.python || process.env.PYTHON || "python3",
		timeoutMs: options.timeoutMs || DEFAULT_TIMEOUT_MS,
	};
	const lessons = listLessonDirs(coursesDir);
	const perLesson = await mapWithConcurrency(
		lessons,
		options.concurrency || os.cpus().length,
		(lesson) => checkLesson(lesson, runOptions)
	);
	return { errors: perLesson.flat(), lessonsChecked: lessons.length };
}

module.exports = { checkCourses };
