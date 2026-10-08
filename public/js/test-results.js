// Turns an execution response for an exercise run into what the lesson page
// shows: a status per listed test, the text for the exercise output panel, and
// whether the exercise passed. Pure, so it can be unit-tested without a DOM.
(function (root) {
	// Strips execution-service job paths from tracebacks.
	function formatOutputText(run) {
		let outputText = "";
		if (run.signal === "SIGKILL") {
			outputText = "Code execution failed";
			if (run.stdout !== "") {
				outputText += ` with output: \n\n${run.stdout}`;
			}
		} else {
			outputText = run.stdout + run.stderr;
		}
		outputText = outputText.replace(/\/piston\/jobs\/[0-9a-zA-Z-].*?'/g, "'"); // replace piston path ends with job id
		outputText = outputText.replace(/\/piston\/jobs\/[0-9a-zA-Z-].*?\//g, ""); // replace piston path following by slash
		outputText = outputText.replace(/\/piston\/jobs\/[0-9a-zA-Z-].*/g, ""); // replace piston path to current job
		outputText = outputText.replace(/\/piston\/packages/g, "");

		if (outputText === "") {
			outputText = "No output";
		}
		return outputText;
	}

	function parseJson(text) {
		try {
			return { ok: true, value: JSON.parse(text) };
		} catch (e) {
			return { ok: false };
		}
	}

	const MAX_VALUE_LENGTH = 200;

	// Strings are shown as-is (test files send Python reprs); anything else as JSON.
	function displayValue(value) {
		const text = typeof value === "string" ? value : JSON.stringify(value);
		if (text.length <= MAX_VALUE_LENGTH) return text;
		const cut = text.length - MAX_VALUE_LENGTH;
		return `${text.slice(0, MAX_VALUE_LENGTH)}… (${cut} more characters)`;
	}

	// A test's result is either a boolean (legacy) or an object with `passed`
	// and optional `got`, `expected`, `error` and `timed_out`.
	function toTestState(id, result) {
		if (result === null || typeof result !== "object") {
			return { id, status: result === true ? "passed" : "failed" };
		}
		if (result.passed === true) {
			return { id, status: "passed" };
		}
		if (result.timed_out === true) {
			return { id, status: "timed_out" };
		}
		const state = {
			id,
			status: result.error !== undefined ? "error" : "failed",
		};
		for (const field of ["got", "expected", "error"]) {
			if (result[field] !== undefined) {
				state[field] = displayValue(result[field]);
			}
		}
		return state;
	}

	// `richResults` marks lessons whose test file uses the object result format.
	// For those, a run killed by the service shows unreported tests as timed out.
	function interpretTestRun(response, listedTestIds, options = {}) {
		const run = response.run;
		const parsed = parseJson(run.stdout);
		const killed = run.signal === "SIGKILL";

		if (options.richResults && killed) {
			const results =
				parsed.ok && parsed.value !== null && typeof parsed.value === "object"
					? parsed.value
					: {};
			const tests = listedTestIds.map((id) =>
				results[id] === undefined
					? { id, status: "timed_out" }
					: toTestState(id, results[id])
			);
			const passedCount = tests.filter((t) => t.status === "passed").length;
			return {
				mode: "tests",
				tests,
				panelText: `##### Tests #####\nTest Result: ${passedCount}/${tests.length}\nThe run was stopped because it took too long.\n`,
				passed: false,
			};
		}

		if (!parsed.ok) {
			// Exercises whose test output isn't JSON pass when nothing went wrong.
			return {
				mode: "raw",
				tests: [],
				panelText: formatOutputText({
					stdout: `##### Exercise #####\n${run.stdout}`,
					stderr: run.stderr,
					signal: run.signal,
				}),
				passed: run.signal !== "SIGKILL" && run.stderr === "",
			};
		}

		const results =
			parsed.value !== null && typeof parsed.value === "object"
				? parsed.value
				: {};
		const tests = listedTestIds.map((id) => toTestState(id, results[id]));
		const passedCount = tests.filter((t) => t.status === "passed").length;

		return {
			mode: "tests",
			tests,
			panelText: `##### Tests #####\nTest Result: ${passedCount}/${tests.length}\n`,
			passed: run.signal !== "SIGKILL" && passedCount === tests.length,
		};
	}

	const api = { interpretTestRun, formatOutputText };
	if (typeof module !== "undefined" && module.exports) {
		module.exports = api;
	} else {
		root.testResults = api;
	}
})(this);
