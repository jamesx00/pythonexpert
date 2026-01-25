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
	let checkExerciseWithJson = false;
	let testResult = null;

	try {
		testResult = JSON.parse(output.run.stdout);
		checkExerciseWithJson = true;
	} catch (e) {}

	if (!checkExerciseWithJson) {
		const executionOutput = {
			run: {
				stdout: `##### Exercise #####\n${output.run.stdout}`,
				stderr: output.run.stderr,
				signal: output.run.signal,
			},
		};

		const passedExercise =
			executionOutput.run.signal !== "SIGKILL" &&
			executionOutput.run.stderr === "";

		state["passedExercise"] = passedExercise;
		updateExecutionOutput(element, executionOutput);
	} else {
		const testCases = document.querySelectorAll("[id^=test-]");
		const passedTestClassName = "list-image-checked";
		const failedTestClassName = "list-image-crossed";
		let passedTests = 0;
		let failedTests = 0;

		for (const testCase of testCases) {
			const testId = parseInt(testCase.id.split("test-")[1]);
			const passedTestCase = testResult[testId] === true;
			const testCaseListItem = document.getElementById(`test-${testId}`);
			if (testCaseListItem === null) continue;
			if (passedTestCase) {
				testCaseListItem.classList.add(passedTestClassName);
				testCaseListItem.classList.remove(failedTestClassName);
				passedTests += 1;
			} else {
				testCaseListItem.classList.add(failedTestClassName);
				testCaseListItem.classList.remove(passedTestClassName);
				failedTests += 1;
			}
		}

		const executionOutput = {
			run: {
				stdout: `##### Tests #####\nTest Result: ${passedTests}/${
					failedTests + passedTests
				}\n`,
				stderr: "",
				signal: null,
			},
		};

		const isPassingTests = output.run.signal !== "SIGKILL" && failedTests === 0;
		state["passedExercise"] = isPassingTests;
		updateExecutionOutput(element, executionOutput);
	}
	state["passedExercise"] && showCompleteAndNextForm();
	!state["passedExercise"] && hideCompleteAndNextForm();
	if (state["passedExercise"] && completeAndNextFormContainers) {
		completeAndNextModalContainer.classList.remove("hidden", "opacity-0");
		completeAndNextModalContainer.querySelector("a").focus();
	}
}

function updateExecutionOutput(element, output) {
	let outputText = "";
	if (output.run.signal === "SIGKILL") {
		outputText = "Code execution failed";
		if (output.run.stdout !== "") {
			outputText += ` with output: \n\n${output.run.stdout}`;
		}
	} else {
		outputText = output.run.stdout + output.run.stderr;
	}
	outputText = outputText.replace(/\/piston\/jobs\/[0-9a-zA-Z-].*?'/g, "'"); // replace piston path ends with job id
	outputText = outputText.replace(/\/piston\/jobs\/[0-9a-zA-Z-].*?\//g, ""); // replace piston path following by slash
	outputText = outputText.replace(/\/piston\/jobs\/[0-9a-zA-Z-].*/g, ""); // replace piston path to current job
	outputText = outputText.replace(/\/piston\/packages/g, "");

	if (outputText === "") {
		outputText = "No output";
	}

	element.innerHTML = hljs.highlight(outputText, { language: "shell" }).value;
}

function executeCode(language, files) {
	const runTimes = {
		python: "3.10.0",
		javascript: "16.3.0",
		typescript: "4.2.3",
	};

	const filesForExecution = files.map((file) => ({
		content: file.content,
		name: file.name,
	}));

	const executionPayload = {
		language: language,
		version: runTimes[language],
		files: filesForExecution,
	};

	const executionUrl =
		localStorage.getItem("execution_endpoint") ||
		"https://execute.pythonexpert.dev/api/v2/execute";
	// const executionUrl = "https://emkc.org/api/v2/piston/execute";

	if (window.rybbit !== undefined) {
		window.rybbit.event("execute_code", {
			page: location.pathname,
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
