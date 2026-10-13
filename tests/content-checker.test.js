const test = require("node:test");
const assert = require("node:assert");
const path = require("path");
const { checkCourses } = require("../scripts/content-checker");

const fixture = (name) =>
	path.join(__dirname, "fixtures", "content-checker", name);

test("a valid lesson produces no errors", async () => {
	const report = await checkCourses(fixture("valid"));
	assert.deepStrictEqual(report.errors, []);
	assert.strictEqual(report.lessonsChecked, 1);
});

test("a reference solution that fails a test is reported with the lesson and test ID", async () => {
	const report = await checkCourses(fixture("reference-fails"));
	assert.deepStrictEqual(report.errors, [
		{
			lesson: "demo/1.1-add",
			testId: 2,
			message: "reference solution fails this test",
		},
	]);
});

test("a starter that already passes every test is reported", async () => {
	const report = await checkCourses(fixture("starter-passes"));
	assert.deepStrictEqual(report.errors, [
		{
			lesson: "demo/1.1-add",
			message: "starter code passes every test; at least one should fail",
		},
	]);
});

test("listed test IDs that differ from the IDs the test file reports are reported", async () => {
	const report = await checkCourses(fixture("mismatched-ids"));
	assert.deepStrictEqual(report.errors, [
		{
			lesson: "demo/1.1-add",
			testId: 2,
			message: "test file reports this test ID but the lesson does not list it",
		},
		{
			lesson: "demo/1.1-add",
			testId: 3,
			message: "lesson lists this test ID but the test file does not report it",
		},
	]);
});

test("front matter that does not parse is reported", async () => {
	const report = await checkCourses(fixture("invalid-front-matter"));
	assert.strictEqual(report.errors.length, 1);
	assert.strictEqual(report.errors[0].lesson, "demo/1.1-add");
	assert.match(report.errors[0].message, /^invalid front matter/);
});

test("a file referenced in front matter that does not exist is reported", async () => {
	const report = await checkCourses(fixture("missing-file"));
	assert.deepStrictEqual(report.errors, [
		{
			lesson: "demo/1.1-add",
			message: 'file "tests.py" referenced in front matter does not exist',
		},
	]);
});

test("the reference replaces the lesson's main file whatever its name, using course common files", async () => {
	const report = await checkCourses(fixture("sql-main-file"));
	assert.deepStrictEqual(report.errors, []);
	assert.strictEqual(report.lessonsChecked, 1);
});

test("valid lesson metadata (difficulty, target complexity, hints) is accepted", async () => {
	const report = await checkCourses(fixture("valid-metadata"));
	assert.deepStrictEqual(report.errors, []);
});

test("invalid lesson metadata is reported field by field", async () => {
	const report = await checkCourses(fixture("invalid-metadata"));
	assert.deepStrictEqual(
		report.errors.map((error) => error.message),
		[
			'difficulty must be one of easy, medium, hard (got "tricky")',
			"target_complexity.time must be a non-empty string",
			"hints must be a list of non-empty strings",
			"checkpoint must be true or false",
		]
	);
	assert.ok(report.errors.every((error) => error.lesson === "demo/1.1-add"));
});

test("a lesson without a reference whose test file crashes instead of printing a result is reported", async () => {
	const report = await checkCourses(fixture("test-file-crashes"));
	assert.deepStrictEqual(report.errors, [
		{
			lesson: "demo/1.1-add",
			message:
				"starter run crashed without printing a JSON result: RuntimeError: broken test file",
		},
	]);
});

test("a checkpoint lesson with hints is reported", async () => {
	const report = await checkCourses(fixture("checkpoint-with-hints"));
	assert.deepStrictEqual(report.errors, [
		{ lesson: "demo/1.1-add", message: "checkpoint lessons must not have hints" },
	]);
});

test("a lesson with a reference but no listed tests reports the unlisted IDs, not a passing starter", async () => {
	const report = await checkCourses(fixture("no-listed-tests"));
	assert.deepStrictEqual(
		report.errors.map((error) => error.message),
		[
			"test file reports this test ID but the lesson does not list it",
			"test file reports this test ID but the lesson does not list it",
		]
	);
});

test("a shipped file with a character the site can't embed is reported with its line", async () => {
	const report = await checkCourses(fixture("non-latin1-file"));
	assert.deepStrictEqual(report.errors, [
		{
			lesson: "demo/1.1-add",
			message:
				'file "main.py" line 2 contains "→" (U+2192), which the site can\'t embed (btoa only accepts Latin-1); use an escape such as \\u2192 instead',
		},
	]);
});
