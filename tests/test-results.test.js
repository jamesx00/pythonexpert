const test = require("node:test");
const assert = require("node:assert");
const { interpretTestRun } = require("../public/js/test-results");
const legacyResponses = require("./fixtures/test-results/legacy-responses.json");

const response = (stdout, extra = {}) => ({
	language: "python",
	version: "3.10.0",
	run: { stdout, stderr: "", code: 0, signal: null, output: stdout, ...extra },
});

for (const recorded of legacyResponses) {
	test(`legacy response keeps today's display: ${recorded.name}`, () => {
		assert.deepStrictEqual(
			interpretTestRun(recorded.response, recorded.listedTestIds),
			recorded.expectedDisplay
		);
	});
}

test("a rich failed result shows what the learner's code returned next to the expected value", () => {
	const display = interpretTestRun(
		response(
			JSON.stringify({
				1: { passed: true },
				2: { passed: false, got: "[0, 1]", expected: "[1, 2]" },
			})
		),
		[1, 2]
	);
	assert.deepStrictEqual(display.tests, [
		{ id: 1, status: "passed" },
		{ id: 2, status: "failed", got: "[0, 1]", expected: "[1, 2]" },
	]);
	assert.strictEqual(display.panelText, "##### Tests #####\nTest Result: 1/2\n");
	assert.strictEqual(display.passed, false);
});

test("a test whose code raised shows the exception type and message", () => {
	const display = interpretTestRun(
		response(
			JSON.stringify({
				1: { passed: false, error: "IndexError: list index out of range", expected: "3" },
			})
		),
		[1]
	);
	assert.deepStrictEqual(display.tests, [
		{ id: 1, status: "error", error: "IndexError: list index out of range", expected: "3" },
	]);
});

test("a test over its time budget is labelled as too slow", () => {
	const display = interpretTestRun(
		response(JSON.stringify({ 1: { passed: true }, 2: { passed: false, timed_out: true } })),
		[1, 2]
	);
	assert.deepStrictEqual(display.tests, [
		{ id: 1, status: "passed" },
		{ id: 2, status: "timed_out" },
	]);
	assert.strictEqual(display.passed, false);
});

test("in a lesson with rich results, a run killed by the service shows every unreported test as timed out", () => {
	const display = interpretTestRun(
		{
			language: "python",
			version: "3.10.0",
			run: { stdout: "", stderr: "", code: null, signal: "SIGKILL", output: "" },
		},
		[1, 2],
		{ richResults: true }
	);
	assert.strictEqual(display.mode, "tests");
	assert.deepStrictEqual(display.tests, [
		{ id: 1, status: "timed_out" },
		{ id: 2, status: "timed_out" },
	]);
	assert.strictEqual(
		display.panelText,
		"##### Tests #####\nTest Result: 0/2\nThe run was stopped because it took too long.\n"
	);
	assert.strictEqual(display.passed, false);
});

test("in a lesson with rich results, tests reported before a kill keep their result", () => {
	const display = interpretTestRun(
		{
			language: "python",
			version: "3.10.0",
			run: { stdout: '{"1": {"passed": true}}', stderr: "", code: null, signal: "SIGKILL", output: "" },
		},
		[1, 2],
		{ richResults: true }
	);
	assert.deepStrictEqual(display.tests, [
		{ id: 1, status: "passed" },
		{ id: 2, status: "timed_out" },
	]);
});

test("very long values are truncated, saying how much was cut", () => {
	const got = "[" + "7, ".repeat(1000) + "7]";
	const display = interpretTestRun(
		response(JSON.stringify({ 1: { passed: false, got, expected: "[]" } })),
		[1]
	);
	assert.strictEqual(
		display.tests[0].got,
		got.slice(0, 200) + `… (${got.length - 200} more characters)`
	);
	assert.strictEqual(display.tests[0].expected, "[]");
});

test("non-string values are shown as JSON", () => {
	const display = interpretTestRun(
		response(JSON.stringify({ 1: { passed: false, got: [1, 2], expected: null } })),
		[1]
	);
	assert.deepStrictEqual(display.tests[0], {
		id: 1,
		status: "failed",
		got: "[1,2]",
		expected: "null",
	});
});
