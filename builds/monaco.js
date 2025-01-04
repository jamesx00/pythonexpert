import { initVimMode } from "monaco-vim";
import * as monaco from "monaco-editor/esm/vs/editor/editor.main.js";

self.MonacoEnvironment = {
	getWorkerUrl: function (moduleId, label) {
		if (label === "json") {
			return "/js/monaco-editor/language/json/json.worker.js";
		}
		if (label === "css" || label === "scss" || label === "less") {
			return "/js/monaco-editor/language/css/css.worker.js";
		}
		if (label === "html" || label === "handlebars" || label === "razor") {
			return "/js/monaco-editor/language/html/html.worker.js";
		}
		if (label === "typescript" || label === "javascript") {
			return "/js/monaco-editor/language/typescript/ts.worker.js";
		}
		return "/js/monaco-editor/editor/editor.worker.js";
	},
};

/**
 * @typedef {number} MonacoFileId
 * @typedef {number} MonacoFileGroupId
 */

/**
 * @typedef {Object} MonacoFile
 * @property {number} id
 * @property {string} content
 * @property {string} file_name
 * @property {string} file_type
 * @property {boolean} is_editable
 * @property {boolean} is_closable
 * @property {boolean} is_edit_focus
 * @property {boolean} is_hidden
 * @property {boolean} is_main
 * @property {boolean} is_test_file
 **/

/**
 * @typedef {Object} MonacoFileGroup
 * @property {number} id
 * @property {string} name
 * @property {MonacoFile[]} files
 * @property {boolean} common
 */

/**
 * @typedef {Object} MultipleFileGroupEditorCallbacks
 * @property {function(MonacoFile): void=} beforeCreateNewFile
 * @property {function(monaco.editor.IStandaloneCodeEditor, MultipleFileGroupEditor): void=} onDidCreateEditor
 * @property {function(MultipleFileGroupEditor): void=} onDidChangeFileGroup
 * @property {function(MonacoFile): void=} onDidCloseFile
 */

/**
 * @typedef {Object} MultipleFileGroupEditorOptions
 * @property {MonacoFileGroup[]} fileGroups
 * @property {string} tabsContainerSelector
 * @property {string} fileGroupSelector
 * @property {string} userLanguage
 * @property {boolean} allowAddFile
 * @property {boolean} showHiddenFiles
 * @property {boolean} vimMode
 * @property {MultipleFileGroupEditorCallbacks=} callbacks
 */

class MultipleFileGroupEditor {
	/**
	 *
	 * @param {string} selector
	 * @param {MultipleFileGroupEditorOptions} options
	 * @param {*=} editorOptions
	 * @returns
	 */
	constructor(selector, options, editorOptions) {
		const { tabsContainerSelector, fileGroupSelector } = options;

		/**
		 * @type {MonacoFileGroupId|null}
		 */
		this.currentFileGroupId = null;

		/**
		 * @type {MonacoFileId|null}
		 */
		this.currentFileId = null;

		this.options = options;
		/**
		 * @type {HTMLElement}
		 */
		// @ts-ignore
		this.editorContainer = document.querySelector(selector);
		if (this.editorContainer === null) {
			throw new Error("Selector not found");
		}

		this.tabsContainer = document.querySelector(tabsContainerSelector);
		if (this.tabsContainer === null) {
			throw new Error("Tabs container selector not found");
		}

		this.fileGroupDropDownContainer = document.querySelector(fileGroupSelector);
		if (this.fileGroupDropDownContainer === null) {
			throw new Error("Tabs container selector not found");
		}

		if (this.fileGroupDropDownContainer.tagName !== "SELECT") {
			throw new Error("File group selector must be a select element");
		}

		this.selector = selector;

		/**
		 * @type {MonacoFileGroup[]}
		 */
		this.fileGroups = JSON.parse(JSON.stringify(options.fileGroups));

		this.editorOptions = {
			// theme: "vs-dark",
			minimap: { enabled: false },
			fontSize: 14,
			padding: { top: 16 },
			fontFamily: "Victor Mono",
			...(editorOptions || {}),
		};

		/**
		 * @type {Record<MonacoFileGroupId, Record<MonacoFileId, {file: MonacoFile, model: monaco.editor.ITextModel}>>}
		 */
		this.models = {};

		/**
		 * @type {Record<number, number>}
		 */
		this.fileGroupMap = {};

		/**
		 * @type {Record<MonacoFileGroupId, MonacoFileId[]>}
		 */
		this.openedFileHistory = {};

		this.initializeModels();

		this.editor = monaco.editor.create(
			this.editorContainer,
			this.editorOptions
		);

		if (options.vimMode) {
			const statusNode = document.getElementById("vim-status");
			initVimMode(this.editor, statusNode);
		}

		this.options.callbacks?.onDidCreateEditor?.(this.editor, this);

		this.initializeTabButtons();
		this.initializeFileGroupDropdown();
		if (this.options.allowAddFile) {
			this.initializeAddNewFile();
		}
	}

	initializeAddNewFile() {
		const { modal, input } = this.createNewFileModal();
		const button = document.createElement("button");
		button.id = "add-new-file-button";
		button.classList.add(
			"px-2",
			"text-gray-300",
			"hover:text-gray-400",
			"text-base"
		);
		button.innerHTML = "+";
		button.addEventListener("click", () => {
			setTimeout(() => {
				input.focus();
			}, 0);
			modal.classList.remove("hidden");
			modal.classList.add("flex");
		});
		this.tabsContainer.appendChild(button);
	}

	/**
	 *
	 * @returns
	 */
	createNewFileModal() {
		const modal = document.createElement("div");
		modal.classList.add(
			"fixed",
			"inset-0",
			"bg-gray-900",
			"bg-opacity-90",
			"justify-center",
			"items-center",
			"hidden"
		);
		const div = document.createElement("div");
		modal.addEventListener("click", (event) => {
			if (event.target === modal) {
				modal.classList.add("hidden");
				modal.classList.remove("flex");
			}
		});
		div.classList.add("bg-white", "p-4", "rounded-lg", "w-96");
		const form = document.createElement("form");
		form.id = "form-new-file";
		form.classList.add("flex", "flex-col");

		const label = document.createElement("label");
		label.setAttribute("for", "file-name");
		label.classList.add("text-sm", "text-gray-700");
		label.textContent = "File Name";
		const input = document.createElement("input");
		input.id = "file-name";
		input.type = "text";
		input.classList.add("border", "border-gray-300", "p-2", "rounded-lg");
		input.required = true;
		const button = document.createElement("button");
		button.type = "submit";
		button.classList.add(
			"bg-blue-500",
			"text-white",
			"p-2",
			"rounded-lg",
			"mt-4"
		);
		button.textContent = "+";
		form.appendChild(label);
		form.appendChild(input);
		form.appendChild(button);
		div.appendChild(form);
		modal.appendChild(div);
		document.body.appendChild(modal);

		form.addEventListener("submit", (event) => {
			event.preventDefault();
			const fileName = input.value;
			this.createNewFile(fileName);
			modal.classList.add("hidden");
			modal.classList.remove("flex");
			input.value = "";
			return false;
		});

		return { modal, input };
	}

	/**
	 *
	 * @param {string} fileName
	 */
	createNewFile(fileName) {
		if (fileName.trim() === "") {
			return;
		}

		const newFileId = Date.now();

		let fileType = this.getFileTypeByFileName(fileName);

		/**
		 * @type {MonacoFile}
		 */
		const newFile = {
			content: "",
			is_editable: true,
			file_name: fileName,
			file_type: fileType,
			is_edit_focus: false,
			is_main: false,
			is_hidden: false,
			id: newFileId,
			is_test_file: false,
			is_closable: true,
		};

		this.options.callbacks?.beforeCreateNewFile?.(newFile);

		if (this.currentFileGroupId === null) return;

		this.models[this.currentFileGroupId][newFileId] = {
			file: newFile,
			model: monaco.editor.createModel(newFile.content, newFile.file_type),
		};
		const newFileButton = this.createTabButton(newFile);
		const addFileButton = document.getElementById("add-new-file-button");
		this.tabsContainer.insertBefore(newFileButton, addFileButton);
		this.fileGroupMap[newFileId] = this.currentFileGroupId;
		this.changeToFile(newFileId);
	}

	/**
	 *
	 * @param {string} fileName
	 * @returns {string}
	 */
	getFileTypeByFileName(fileName) {
		if (fileName.endsWith(".md")) return "markdown";
		if (fileName.endsWith(".css")) return "css";
		if (fileName.endsWith(".html")) return "html";
		if (fileName.endsWith(".py")) return "python";
		if (fileName.endsWith(".js")) return "javascript";
		if (fileName.endsWith(".ts")) return "typescript";
		if (fileName.endsWith(".sql")) return "sql";
		return "plaintext";
	}

	initializeModels() {
		for (const fileGroup of this.fileGroups) {
			this.models[fileGroup.id] = {};
			this.models[fileGroup.id]["fileGroup"] = fileGroup;
			for (const file of fileGroup.files) {
				const fileType = this.getFileTypeByFileName(file.file_name);
				this.fileGroupMap[file.id] = fileGroup.id;
				const fileContent = this.translateContent(file.content);
				this.models[fileGroup.id][file.id] = {
					file: file,
					model: monaco.editor.createModel(fileContent, fileType),
				};
			}
		}
	}

	translateContent(content) {
		const fileContentTranslateMap = {
			en: {
				write_your_code_below_this_line: "Write your code below this line",
				write_your_code_above_this_line: "Write your code above this line",
				edit_the_code_below_this_line: "Edit the code below this line",
				edit_the_code_above_this_line: "Edit the code above this line",
			},
			th: {
				write_your_code_below_this_line: "เขียนโค้ดใต้บรรทัดนี้",
				write_your_code_above_this_line: "เขียนโค้ดเหนือบรรทัดนี้",
				edit_the_code_below_this_line: "แก้ไขโค้ดใต้บรรทัดนี้",
				edit_the_code_above_this_line: "แก้ไขโค้ดเหนือบรรทัดนี้",
			},
		};

		const textToTranslate = fileContentTranslateMap[this.options.userLanguage];
		let result = content;
		for (const key in textToTranslate) {
			result = result.replaceAll(key, textToTranslate[key]);
		}
		return result;
	}

	initializeFileGroupDropdown() {
		for (const fileGroup of this.fileGroups) {
			if (fileGroup.common) continue;

			const option = document.createElement("option");
			option.setAttribute("value", String(fileGroup.id));
			option.textContent = fileGroup.name;
			this.fileGroupDropDownContainer.appendChild(option);
		}
		if (this.fileGroupDropDownContainer.classList.contains("hidden")) {
			this.fileGroupDropDownContainer.classList.remove("hidden");
		}

		this.fileGroupDropDownContainer.addEventListener("change", (event) => {
			this.changeToFileGroup(parseInt(this.fileGroupDropDownContainer.value));
		});

		this.changeToFileGroup(parseInt(this.fileGroupDropDownContainer.value));
	}

	/**
	 *
	 * @param {number} fileGroupId
	 */
	changeToFileGroup(fileGroupId) {
		const fileIdsInGroup = this.getFileIdsFromGroupId(fileGroupId);
		const commonFileIds = this.getCommonFileIds();
		const fileIdsToDisplay = [...fileIdsInGroup, ...commonFileIds];
		const allTabButtons = this.getAllTabButtons();

		for (const tabButton of allTabButtons) {
			tabButton.classList.add("hidden");
		}

		for (const fileId of fileIdsToDisplay) {
			const tabButtonId = `file-${fileId}`;
			const tabButton = document.getElementById(tabButtonId);
			tabButton?.classList.remove("hidden");
		}

		const filesAndModels = this.getFilesAndModelsFromGroupId(fileGroupId);
		const fileIds = this.getFileIdsFromGroupId(fileGroupId);
		/**
		 * @type {MonacoFile[]}
		 */
		const files = [];
		for (const fileId of fileIds) {
			/**
			 * @type {MonacoFile}
			 */
			const file = filesAndModels[fileId].file;
			if (file.is_hidden) continue;
			files.push(filesAndModels[fileId].file);
		}

		const sortedFileIds = files.sort((file1, file2) => {
			if (file1.is_edit_focus) return -1;
			return 1;
		});

		sortedFileIds.length > 0 && this.changeToFile(sortedFileIds[0].id);

		this.currentFileGroupId = fileGroupId;
		this.options.callbacks?.onDidChangeFileGroup?.(this);
	}

	/**
	 *
	 * @returns
	 */
	getAllTabButtons() {
		return document.querySelectorAll(
			'#file-buttons-container > button[id^="file-"]'
		);
	}

	/**
	 * Reset all tab buttons to default style (not-selected)
	 */
	resetTabButtons() {
		const buttons = this.getAllTabButtons();
		for (const button of buttons) {
			button.classList.remove("border-x-2", "bg-gray-200", "text-gray-800");
			const closeTabIcon = button.querySelector('svg[data-action="closeTab"]');
			closeTabIcon && closeTabIcon.classList.add("hidden");
		}
	}

	/**
	 *
	 * @param {number} fileId
	 */
	changeToFile(fileId) {
		this.currentFileId = fileId;
		this.addFileToHistory(fileId);
		const model = this.getModelFromFileId(fileId);
		this.editor.setModel(model);

		const file = this.getFileFromFileId(fileId);
		this.editor.updateOptions({ readOnly: !file.is_editable });
		this.resetTabButtons();
		const selectedFileTabButton = document.getElementById(`file-${fileId}`);
		if (selectedFileTabButton) {
			selectedFileTabButton.classList.add(
				"border-x-2",
				"bg-gray-200",
				"text-gray-800"
			);
			const closeTabIcon = selectedFileTabButton.querySelector(
				'svg[data-action="closeTab"]'
			);
			closeTabIcon && closeTabIcon.classList.remove("hidden");
		}
	}

	/**
	 *
	 * @param {MonacoFileId} fileId
	 */
	addFileToHistory(fileId) {
		const currentFileGroupId = this.currentFileGroupId;
		if (currentFileGroupId === null) return;
		this.openedFileHistory[currentFileGroupId] =
			this.openedFileHistory[currentFileGroupId] || [];
		if (
			this.openedFileHistory[currentFileGroupId][
				this.openedFileHistory[currentFileGroupId].length - 1
			] !== fileId
		) {
			this.openedFileHistory[currentFileGroupId].push(fileId);
		}
	}

	/**
	 *
	 * @param {MonacoFileId} fileId
	 */
	closeFile(fileId) {
		const currentFileGroupId = this.currentFileGroupId;
		if (currentFileGroupId === null) return;

		const file = this.getFileFromFileId(fileId);

		this.openedFileHistory[currentFileGroupId]?.pop();
		const previouslyOpenedFileId =
			this.openedFileHistory[currentFileGroupId]?.pop();

		if (previouslyOpenedFileId !== undefined) {
			this.changeToFile(previouslyOpenedFileId);
		} else {
			this.changeToFileGroup(currentFileGroupId);
		}
		this.disposeModelByFileId(fileId);

		const tabButton = document.getElementById(`file-${fileId}`);
		tabButton && tabButton.remove();

		this.removeFileIdFromHistory(fileId);

		this.options.callbacks?.onDidCloseFile?.(file);
	}

	/**
	 *
	 * @param {MonacoFileId} fileId
	 */
	removeFileIdFromHistory(fileId) {
		const fileGroupIds = Object.keys(this.openedFileHistory);
		for (const fileGroupId of fileGroupIds) {
			const history = this.openedFileHistory[fileGroupId];
			var i = 0;
			while (i < history.length) {
				if (history[i] === fileId) {
					history.splice(i, 1);
				} else {
					++i;
				}
			}
		}
	}

	disposeModelByFileId(fileId) {
		const fileGroupId = this.getFileGroupIdFromFileId(fileId);
		this.models[fileGroupId][fileId].model.dispose();
		delete this.models[fileGroupId][fileId];
	}

	/**
	 *
	 * @returns {number[]}
	 */
	getCommonFileIds() {
		const commonFileGroupIds = this.fileGroups
			.filter((fg) => fg.common)
			.map((fg) => fg.id);
		const result = [];
		for (const fileGroupId of commonFileGroupIds) {
			const fileIds = this.getFileIdsFromGroupId(fileGroupId);
			result.push(...fileIds);
		}
		return result;
	}

	/**
	 *
	 * @param {MonacoFileGroupId} fileGroupId
	 * @returns {number[]}
	 */
	getFileIdsFromGroupId(fileGroupId) {
		const files = this.getFilesAndModelsFromGroupId(fileGroupId);
		return Object.keys(files)
			.filter((k) => !isNaN(k))
			.map((k) => parseInt(k));
	}

	/**
	 *
	 * @returns
	 */
	getFilesAndModelsFromCurrentFileGroup() {
		if (this.currentFileGroupId === null) return {};
		return {
			...this.getFilesAndModelsFromGroupId(this.currentFileGroupId),
			...this.getFilesAndModelsFromCommonFileGroups(),
		};
	}

	/**
	 *
	 * @returns
	 */
	getFilesAndModelsFromCommonFileGroups() {
		const commonFileGroupIds = this.fileGroups
			.filter((fg) => fg.common)
			.map((fg) => fg.id);
		/**
		 * @type {Record<number, {file: MonacoFile, model: monaco.editor.ITextModel}>}
		 */
		const result = {};
		for (const fileGroupId of commonFileGroupIds) {
			const files = this.getFilesAndModelsFromGroupId(fileGroupId);
			for (const fileId in files) {
				result[fileId] = files[fileId];
			}
		}
		return result;
	}

	/**
	 *
	 * @param {*} fileGroupId
	 * @returns
	 */
	getFilesAndModelsFromGroupId(fileGroupId) {
		const result = this.models[fileGroupId];
		delete result["fileGroup"];
		return result;
	}

	/**
	 * Check if the current file group has a test file or not
	 * @returns {boolean}
	 */
	currentFileGroupHasTestFile() {
		const currentFileGroup = this.currentFileGroupId;
		if (currentFileGroup === null) return false;
		const filesAndModels = this.getFilesAndModelsFromCurrentFileGroup();
		let hasTestFile = false;
		for (const [_, value] of Object.entries(filesAndModels)) {
			const { file } = value;
			if (file.is_test_file) {
				hasTestFile = true;
				break;
			}
		}
		return hasTestFile;
	}

	/**
	 * @returns {MonacoFile[]}
	 */
	getAllFiles() {
		/**
		 * @type {MonacoFile[]}
		 */
		const result = [];
		for (const fileGroup of this.fileGroups) {
			for (const file of fileGroup.files) {
				result.push(file);
			}
		}
		return result;
	}

	/**
	 *
	 * @param {MonacoFileId} fileId
	 * @returns {MonacoFileGroupId}
	 */
	getFileGroupIdFromFileId(fileId) {
		return this.fileGroupMap[fileId];
	}

	/**
	 *
	 * @param {MonacoFileId} fileId
	 * @returns {MonacoFile}
	 */
	getFileFromFileId(fileId) {
		const fileGroupId = this.getFileGroupIdFromFileId(fileId);
		return this.models[fileGroupId][fileId].file;
	}

	/**
	 *
	 * @param {MonacoFileId} fileId
	 * @returns
	 */
	getModelFromFileId(fileId) {
		const fileGroupId = this.getFileGroupIdFromFileId(fileId);
		return this.models[fileGroupId][fileId].model;
	}

	initializeTabButtons() {
		const files = this.getAllFiles().sort((file1, file2) => {
			if (file1.is_edit_focus) return -1;
			return 1;
		});
		for (const file of files) {
			if (this.options.showHiddenFiles || !file.is_hidden) {
				const button = this.createTabButton(file, true);
				this.tabsContainer.appendChild(button);
			}
		}
	}

	/**
	 * @param {MonacoFile} file
	 * @param {boolean=} hide
	 */
	createTabButton(file, hide = false) {
		const button = document.createElement("button");
		button.id = `file-${file.id}`;
		button.classList.add("editor-tab");
		if (hide) {
			button.classList.add("hidden");
		}
		let buttonContent = file.file_name;
		if (file.is_hidden) {
			buttonContent = `
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4 inline">
							<path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 0 0 1.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.451 10.451 0 0 1 12 4.5c4.756 0 8.773 3.162 10.065 7.498a10.522 10.522 0 0 1-4.293 5.774M6.228 6.228 3 3m3.228 3.228 3.65 3.65m7.894 7.894L21 21m-3.228-3.228-3.65-3.65m0 0a3 3 0 1 0-4.243-4.243m4.242 4.242L9.88 9.88" />
						</svg>
					${buttonContent}`;
		}

		button.innerHTML = buttonContent;

		if (file.is_closable) {
			const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
			svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
			svg.setAttribute("data-action", "closeTab");
			svg.setAttribute("fill", "none");
			svg.setAttribute("viewBox", "0 0 24 24");
			svg.setAttribute("stroke-width", "1.5");
			svg.setAttribute("stroke", "currentColor");
			svg.classList.add("w-4", "h-4", "inline-block", "ml-2");
			svg.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />`;
			button.appendChild(svg);
			svg.addEventListener("click", (event) => {
				event.preventDefault();
				event.stopPropagation();
				this.closeFile(file.id);
				return false;
			});
		}

		button.addEventListener("click", () => {
			this.changeToFile(file.id);
		});

		return button;
	}
}

module.exports = {
	MultipleFileGroupEditor,
	monaco,
};
