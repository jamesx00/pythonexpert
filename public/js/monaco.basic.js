// @ts-check

/**
 * @typedef {import('./index.js').MonacoFile} MonacoFile
 * @typedef {import('./index.js').MonacoFileGroup} MonacoFileGroup
 * @typedef {import('./index.js').MultipleFileGroupEditorOptions} MultipleFileGroupEditorOptions
 * @typedef {import('./index.js').MultipleFileGroupEditor} MultipleFileGroupEditor
 */

require(["vs/editor/editor.main"], function () {
	/**
	 * @type {MonacoFileGroup[]}
	 */
	let fileGroups = [
		{
			id: 0,
			name: "File Group 1",
			common: false,
			files: [
				{
					id: Date.now(),
					content: "### This is going to be amazing!",
					file_name: "file1.md",
					file_type: "markdown",
					editable: true,
					is_closable: true,
					is_hidden: false,
					is_edit_focus: true,
					is_main: true,
					is_test_file: false,
				},
			],
		},
	];

	const localStorageFiles = localStorage.getItem("files");
	if (localStorageFiles === null) {
		localStorage.setItem("files", JSON.stringify(fileGroups));
	} else {
		fileGroups = JSON.parse(localStorageFiles);
	}

	let parseMarkdownTimeout = null;

	const multipleFileGroupEditor = new MultipleFileGroupEditor(
		"#editor",
		{
			fileGroups: fileGroups,
			tabsContainerSelector: "#file-buttons-container",
			fileGroupSelector: "#file-group",
			userLanguage: getUserLanguage(),
			allowAddFile: true,
			showHiddenFiles: true,
			callbacks: {
				onDidCloseFile: (monacoFile) => {
					const fileIndex = fileGroups[0].files
						.map((f) => f.id)
						.indexOf(monacoFile.id);
					fileGroups[0].files.splice(fileIndex, 1);
					localStorage.setItem("files", JSON.stringify(fileGroups));
				},
				beforeCreateNewFile: (monacoFile) => {
					const copyFile = { ...monacoFile };
					fileGroups[0].files.push(copyFile);
				},
				onDidCreateEditor: (editor, multipleFileGroupEditor) => {
					editor.onDidChangeModelContent((e, args) => {
						const currentFileId = multipleFileGroupEditor.currentFileId || 0;

						const fileIndex = fileGroups[0].files
							.map((f) => f.id)
							.indexOf(currentFileId);
						const model = editor.getModel();
						const fileContent = model.getValue();
						fileGroups[0].files[fileIndex].content = fileContent;

						setMarkdownDelay(fileContent);
						localStorage.setItem("files", JSON.stringify(fileGroups));
					});

					editor.onDidChangeModel((e, args) => {
						const fileContent = editor.getModel().getValue();
						setMarkdownDelay(fileContent);
						const currentFileId = multipleFileGroupEditor.currentFileId || 0;
						const fileIndex = fileGroups[0].files
							.map((f) => f.id)
							.indexOf(currentFileId);
						fileGroups[0].files[fileIndex].content = fileContent;

						localStorage.setItem("files", JSON.stringify(fileGroups));
					});
				},
			},
		},
		{ wordWrap: "on" }
	);

	function setMarkdownDelay(content, delay = 500) {
		const output = document.getElementById("output");
		if (output === null) {
			throw new Error("Output element not found");
		}

		if (parseMarkdownTimeout !== null) {
			clearTimeout(parseMarkdownTimeout);
		}
		parseMarkdownTimeout = setTimeout(() => {
			getMarkdown(content)
				.then((parsedMarkdown) => {
					output.innerHTML = parsedMarkdown;
					parseMarkdownTimeout = null;
				})
				.then(addCopyBlock)
				.then(processMermaid);
		}, delay);
	}

	async function getMarkdown(fileContent) {
		const csrfToken = getCookie("csrftoken") || "";
		const formData = new FormData();
		formData.append("content", fileContent);
		// const response = await fetch("/markdownx/markdownify/", {
		// 	method: "post",
		// 	headers: {
		// 		"X-CSRFToken": csrfToken,
		// 	},
		// 	body: formData,
		// });
		// const responseBody = await response.text();
		return marked.parse(fileContent);
		// return responseBody;
	}

	async function processMermaid() {
		mermaid.initialize({
			startOnLoad: false,
			fontFamily: "Victor Mono",
			securityLevel: "antiscript",
			theme: "dark",
		});
		await mermaid.run();
	}
});
