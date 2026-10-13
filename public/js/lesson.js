const completeAndNextModalContainer = document.getElementById(
	"complete-and-next-modal-container"
);
const completeAndNextFormContainers = document.querySelectorAll(
	".complete-and-next-form-container"
);
const codeRunningButton = document.getElementById("button-run-code-running");
const executionOutput = document.getElementById("execution-output");
const exerciseOutput = document.getElementById("exercise-output");
const executingOutput = document.getElementById("executing-output");

function hideCompleteAndNextForm() {
	for (const container of completeAndNextFormContainers) {
		const div = container.querySelector("div");
		div && div.classList.add("hidden");
	}
}

function showCompleteAndNextForm() {
	for (const container of completeAndNextFormContainers) {
		const div = container.querySelector("div");
		div && div.classList.remove("hidden");
	}
}

/**
 * @type {MonacoFileGroup[]}
 */
const beforeParsedFileGroups = JSON.parse(
	document.getElementById("file_groups").textContent
);

const parsedFileGroups = beforeParsedFileGroups.map((fileGroup) => {
	fileGroup.files = fileGroup.files.map((file) => {
		const fileId = `${fileGroup.id}-${file.id}`;

		const fileContentFromLocalStorage = localStorage.getItem(
			`files.${location.pathname}.${fileGroup.id}.${file.id}`
		);

		if (
			fileContentFromLocalStorage !== null &&
			fileContentFromLocalStorage !== ""
		) {
			file.content = fileContentFromLocalStorage;
		} else {
			const contentInBase64 =
				document.getElementById(`file-${fileId}`)?.textContent || "";
			file.content = atob(contentInBase64);
		}

		return file;
	});
	return fileGroup;
});

const isAddingFileAllowedElement = document.getElementById(
	"adding_file_allowed"
);
const isAddingFilesAllowed =
	isAddingFileAllowedElement !== null &&
	isAddingFileAllowedElement.textContent === "true";
const multipleFileGroupEditor = new pe.MultipleFileGroupEditor("#editor", {
	fileGroups: parsedFileGroups,
	tabsContainerSelector: "#file-buttons-container",
	fileGroupSelector: "#file-group",
	userLanguage: getUserLanguage(),
	allowAddFile: isAddingFilesAllowed,
	vimMode: localStorage.getItem("editor.vimMode") === "true",
	showHiddenFiles: localStorage.getItem("editor.showHiddenFiles") === "true",
	callbacks: {
		onDidChangeFileGroup: (multipleFileGroupEditor) => {
			const fileGroupHasTest =
				multipleFileGroupEditor.currentFileGroupHasTestFile();
			if (fileGroupHasTest) {
				hideCompleteAndNextForm();
			} else {
				showCompleteAndNextForm();
			}
		},
		onDidCreateEditor(editor, multipleFileGroupEditor) {
			editor.onDidChangeModelContent((e, args) => {
				const fileId = multipleFileGroupEditor.currentFileId || 0;
				const fileGroupId =
					multipleFileGroupEditor.getFileGroupIdFromFileId(fileId);
				const model = editor.getModel();
				const fileContent = model.getValue();
				const key = `files.${location.pathname}.${fileGroupId}.${fileId}`;
				localStorage.setItem(key, fileContent);
			});
		},
	},
});

const editor = multipleFileGroupEditor.editor;
editor.focus();
editor.addAction({
	id: "execute-code",
	label: "Execute the code",
	keybindings: [pe.monaco.KeyMod.WinCtrl | pe.monaco.KeyCode.Enter],
	run: () => {
		runCodeButton &&
			!runCodeButton.classList.contains("hidden") &&
			runCodeButton.click();
	},
});

editor.addAction({
	id: "execute-code-2",
	label: "Execute the code ",
	keybindings: [pe.monaco.KeyMod.CtrlCmd | pe.monaco.KeyCode.Enter],
	run: () => {
		runCodeButton &&
			!runCodeButton.classList.contains("hidden") &&
			runCodeButton.click();
	},
});

const state = {
	passedExercise: false,
};

// Handle run code button
const runCodeButton = document.getElementById("button-run-code");

hotkeys("ctrl+enter", function (event, handler) {
	runCodeButton &&
		!runCodeButton.classList.contains("hidden") &&
		runCodeButton.click();
});

const executingAnimation =
	document.getElementById("executing-output") &&
	new Typed("#executing-output > span", {
		strings: ["Beep...Boop...Beep...Boop...", "Beep...Boop...Zeep..."],
		typeSpeed: 50,
		backSpeed: 30,
		cursorChar: "_",
	});

if (runCodeButton !== null) {
	runCodeButton.addEventListener("click", async (event) => {
		executingAnimation && executingAnimation.reset();
		runCodeButton.classList.add("hidden");
		codeRunningButton && codeRunningButton.classList.remove("hidden");
		executingOutput && executingOutput.classList.remove("hidden");
		executionOutput && executionOutput.classList.add("hidden");
		exerciseOutput && exerciseOutput.classList.add("hidden");

		// const files = [];
		// const selectedFileGroupId = state['selectedFileGroupId'];
		// const fileKeys = Object.keys(state['models'][selectedFileGroupId]).filter(
		// 	(k) => !isNaN(k)
		// );
		/**
		 * @type {{name: string, content: string, is_main: boolean, is_test_file: boolean, language: string}[]}
		 */
		const files = [];
		const filesAndModels =
			multipleFileGroupEditor.getFilesAndModelsFromCurrentFileGroup();
		for (const key of Object.keys(filesAndModels)) {
			/**
			 * @type {MonacoFile}
			 */
			const file = filesAndModels[key].file;
			const model = filesAndModels[key].model;
			files.push({
				name: file.file_name,
				content: model.getValue(),
				is_main: file.is_main,
				is_test_file: file.is_test_file,
				language: file.file_type,
			});
		}

		const sortedFilesToExecute = files
			.sort((file1, _file2) => (file1.is_main ? -1 : 1))
			.sort((file1, _file2) => (file1.is_test_file ? -1 : 1));

		const language = sortedFilesToExecute[0].language || "python";

		const requests = [];

		requests.push(
			executeCode(
				language,
				sortedFilesToExecute.filter((file) => !file.is_test_file)
			)
		);

		const hasTest = multipleFileGroupEditor.currentFileGroupHasTestFile();

		if (hasTest) {
			requests.push(executeCode(language, sortedFilesToExecute));
		}

		const executionResults = await Promise.all(requests);
		runCodeButton.classList.remove("hidden");
		codeRunningButton && codeRunningButton.classList.add("hidden");
		executingOutput && executingOutput.classList.add("hidden");
		executionOutput && executionOutput.classList.remove("hidden");

		if (hasTest) {
			exerciseOutput && exerciseOutput.classList.remove("hidden");
		}

		updateExecutionOutput(executionOutput, await executionResults[0].json());

		hasTest &&
			exerciseOutput &&
			checkExerciseOutput(exerciseOutput, await executionResults[1].json());
	});
}

function checkExerciseOutput(element, output) {
	const testCaseListItems = [];
	for (const testCase of document.querySelectorAll("[id^=test-]")) {
		const testId = parseInt(testCase.id.split("test-")[1]);
		const testCaseListItem = document.getElementById(`test-${testId}`);
		if (testCaseListItem !== null) {
			testCaseListItems.push({ testId, testCaseListItem });
		}
	}

	const display = testResults.interpretTestRun(
		output,
		testCaseListItems.map(({ testId }) => testId),
		{ richResults: document.getElementById("rich_test_results") !== null }
	);

	if (display.mode === "tests") {
		display.tests.forEach((test, index) => {
			renderTestCase(testCaseListItems[index].testCaseListItem, test);
		});
	}

	state["passedExercise"] = display.passed;
	element.innerHTML = hljs.highlight(display.panelText, {
		language: "shell",
	}).value;

	state["passedExercise"] && showCompleteAndNextForm();
	!state["passedExercise"] && hideCompleteAndNextForm();
	if (state["passedExercise"] && completeAndNextFormContainers) {
		completeAndNextModalContainer.classList.remove("hidden", "opacity-0");
		completeAndNextModalContainer.querySelector("a").focus();
	}
}

function renderTestCase(testCaseListItem, test) {
	const passedTestClassName = "list-image-checked";
	const failedTestClassName = "list-image-crossed";
	const passed = test.status === "passed";
	testCaseListItem.classList.add(passed ? passedTestClassName : failedTestClassName);
	testCaseListItem.classList.remove(passed ? failedTestClassName : passedTestClassName);

	testCaseListItem.querySelector(".test-feedback")?.remove();
	const lines = [];
	if (test.status === "timed_out") {
		lines.push("Too slow: took longer than the time limit for this test.");
	}
	if (test.error !== undefined) lines.push(`Error: ${test.error}`);
	if (test.got !== undefined) lines.push(`Got: ${test.got}`);
	if (test.expected !== undefined) lines.push(`Expected: ${test.expected}`);
	if (lines.length === 0) return;

	const feedback = document.createElement("pre");
	feedback.className =
		"test-feedback not-prose mt-1 whitespace-pre-wrap break-words bg-slate-800 p-2 font-victor-mono text-xs text-term-text";
	feedback.textContent = lines.join("\n");
	testCaseListItem.appendChild(feedback);
}

function updateExecutionOutput(element, output) {
	const outputText = testResults.formatOutputText(output.run);
	element.innerHTML = hljs.highlight(outputText, { language: "shell" }).value;
}

function executeCode(language, files) {
	const filesForExecution = files.map((file) => ({
		content: file.content,
		name: file.name,
	}));

	const executionPayload = {
		language: language,
		version: EXPECTED_RUNTIMES[language],
		files: filesForExecution,
	};

	const executionUrl =
		localStorage.getItem("execution_endpoint") ||
		"https://execute.pythonexpert.dev/api/v2/execute";
	// const executionUrl = "https://emkc.org/api/v2/piston/execute";

	if (window.rybbit !== undefined) {
		window.rybbit.event("execute_code", {
			page: location.pathname,
			language: language,
			version: EXPECTED_RUNTIMES[language],
		});
	}

	return fetch(executionUrl.replaceAll('"', ""), {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(executionPayload),
	}).catch((_) => {
		alert("Something went wrong during code execution. Please try again");
	});
}
