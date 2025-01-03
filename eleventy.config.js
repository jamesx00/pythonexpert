const { DateTime } = require("luxon");
const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");
const markdownItAnchor = require("markdown-it-anchor");
// const pluginMermaid = require("@kevingimbel/eleventy-plugin-mermaid");
// const markdownPrismJs = require("@11ty/eleventy-plugin-syntaxhighlight/src/markdownSyntaxHighlightOptions");
const hljs = require("highlight.js");

const pluginRss = require("@11ty/eleventy-plugin-rss");
const pluginBundle = require("@11ty/eleventy-plugin-bundle");
const pluginNavigation = require("@11ty/eleventy-navigation");
const { EleventyHtmlBasePlugin } = require("@11ty/eleventy");

const pluginDrafts = require("./eleventy.config.drafts.js");
const pluginImages = require("./eleventy.config.images.js");
const customCollections = require("./eleventy.config.collection.js");

/** @param {import('@11ty/eleventy').UserConfig} eleventyConfig */
module.exports = function (eleventyConfig) {
	eleventyConfig.ignores.add("./src/courses/*/*/files/**/*");
	eleventyConfig.addMarkdownHighlighter((str, language) => {
		if (language === "mermaid") {
			return `<pre class="mermaid">${str}</pre>`;
		}
		if (language === "") {
			language = "plaintext";
		}
		return hljs.highlight(str, { language }).value;
	});
	// To Support .yaml Extension in _data
	// You may remove this if you can use JSON
	eleventyConfig.addDataExtension("yaml", (contents) => yaml.load(contents));

	// Copy the contents of the `public` folder to the output folder
	// For example, `./public/css/` ends up in `_site/css/`
	eleventyConfig.addPassthroughCopy({
		"./public/": "/",
		"./node_modules/prismjs/themes/prism-okaidia.css": "/css/prism-okaidia.css",
		"./node_modules/alpinejs/dist/cdn.min.js": "/js/alpine.js",
		"./node_modules/@alpinejs/intersect/dist/cdn.min.js":
			"/js/alpine.intersect.js",
		"./node_modules/@alpinejs/persist/dist/cdn.min.js": "/js/alpine.persist.js",
		"./node_modules/hotkeys-js/dist/hotkeys.js": "/js/hotkeys.js",
		"./node_modules/mermaid/dist/mermaid.js": "/js/mermaid.js",
		"./node_modules/typed.js/dist/typed.umd.js": "/js/typed.umd.js",
		"./node_modules/marked/marked.min.js": "/js/marked.min.js",
		"./node_modules/monaco-editor/min": "/js/monaco-editor/min",
		"./src/admin/config.yml": "./admin/config.yml",
		"./src/static/img": "/static/img",
	});

	// Run Eleventy when these files change:
	// https://www.11ty.dev/docs/watch-serve/#add-your-own-watch-targets

	// Watch content images for the image pipeline.
	eleventyConfig.addWatchTarget("src/**/*.{svg,webp,png,jpeg,py,txt,sql,ts}");

	// App plugins
	eleventyConfig.addPlugin(pluginDrafts);
	eleventyConfig.addPlugin(pluginImages);
	eleventyConfig.addPlugin(customCollections);

	// Official plugins
	eleventyConfig.addPlugin(pluginRss);
	eleventyConfig.addPlugin(pluginNavigation);
	eleventyConfig.addPlugin(EleventyHtmlBasePlugin);
	eleventyConfig.addPlugin(pluginBundle);

	// Filters
	eleventyConfig.addFilter("readableDate", (dateObj, format, zone) => {
		// Formatting tokens for Luxon: https://moment.github.io/luxon/#/formatting?id=table-of-tokens
		return DateTime.fromJSDate(dateObj, { zone: zone || "utc" }).toFormat(
			format || "dd LLLL yyyy"
		);
	});

	eleventyConfig.addFilter("htmlDateString", (dateObj) => {
		// dateObj input: https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string
		return DateTime.fromJSDate(dateObj, { zone: "utc" }).toFormat("yyyy-LL-dd");
	});

	// Get the first `n` elements of a collection.
	eleventyConfig.addFilter("head", (array, n) => {
		if (!Array.isArray(array) || array.length === 0) {
			return [];
		}
		if (n < 0) {
			return array.slice(n);
		}

		return array.slice(0, n);
	});

	// Return the smallest number argument
	eleventyConfig.addFilter("min", (...numbers) => {
		return Math.min.apply(null, numbers);
	});

	// Return all the tags used in a collection
	eleventyConfig.addFilter("getAllTags", (collection) => {
		let tagSet = new Set();
		for (let item of collection) {
			(item.data.tags || []).forEach((tag) => tagSet.add(tag));
		}
		return Array.from(tagSet);
	});

	eleventyConfig.addFilter("filterTagList", function filterTagList(tags) {
		return (tags || []).filter(
			(tag) => ["all", "nav", "post", "posts"].indexOf(tag) === -1
		);
	});

	// Customize Markdown library settings:
	eleventyConfig.amendLibrary("md", (mdLib) => {
		mdLib.use(markdownItAnchor, {
			permalink: markdownItAnchor.permalink.ariaHidden({
				placement: "after",
				class: "header-anchor",
				symbol: "#",
				ariaHidden: false,
			}),
			level: [1, 2, 3, 4],
			slugify: eleventyConfig.getFilter("slugify"),
		});
	});

	eleventyConfig.addShortcode("currentBuildDate", () => {
		return new Date().toISOString();
	});

	eleventyConfig.addShortcode("fileContent", (inputPath, fileName) => {
		const directory = path.dirname(inputPath);
		const fullPath = path.join(directory, "files", fileName);
		try {
			return btoa(fs.readFileSync(fullPath, "utf-8"));
		} catch (e) {
			// read from one directory up to common course files
			const directory = path.dirname(path.dirname(inputPath));
			const fullPath = path.join(directory, "files", fileName);
			return btoa(fs.readFileSync(fullPath, "utf-8"));
		}
	});

	// Features to make your build faster (when you need them)

	// If your passthrough copy gets heavy and cumbersome, add this line
	// to emulate the file copy on the dev server. Learn more:
	// https://www.11ty.dev/docs/copy/#emulate-passthrough-copy-during-serve

	// eleventyConfig.setServerPassthroughCopyBehavior("passthrough");

	return {
		// Control which files Eleventy will process
		// e.g.: *.md, *.njk, *.html, *.liquid
		templateFormats: ["md", "njk", "html", "liquid"],

		// Pre-process *.md files with: (default: `liquid`)
		markdownTemplateEngine: "njk",

		// Pre-process *.html files with: (default: `liquid`)
		htmlTemplateEngine: "njk",

		// These are all optional:
		dir: {
			input: "src", // default: "."
			includes: "../_includes", // default: "_includes"
			data: "../_data", // default: "_data"
			output: "_site",
		},

		// -----------------------------------------------------------------
		// Optional items:
		// -----------------------------------------------------------------

		// If your site deploys to a subdirectory, change `pathPrefix`.
		// Read more: https://www.11ty.dev/docs/config/#deploy-to-a-subdirectory-with-a-path-prefix

		// When paired with the HTML <base> plugin https://www.11ty.dev/docs/plugins/html-base/
		// it will transform any absolute URLs in your HTML to include this
		// folder name and does **not** affect where things go in the output folder.
		pathPrefix: "/",
	};
};
