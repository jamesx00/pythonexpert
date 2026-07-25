const path = require("path");

module.exports = function (eleventyConfig) {
	eleventyConfig.addFilter("field", (array, field) => {
		const result = array.map((i) => {
			return i.data[field];
		});
		return result;
	});

	eleventyConfig.addFilter("filter", (array, field, value) => {
		return array.filter((i) => {
			return i.data[field] === value;
		});
	});

	eleventyConfig.addFilter("unique", (array) => {
		return [...new Set(array)];
	});

	const getNumberPrefix = (inputPath) => {
		const dirName = path.basename(path.dirname(inputPath));
		const prefix = dirName.split("-")[0];
		const [beforeDecimal, afterDecimal] = prefix.split(".").map(Number);
		return [beforeDecimal, afterDecimal || 0];
	};

	// The integer folder prefix (e.g. 1 for "1.3-what-is-a-database") used to
	// group lessons into the same sidebar folder.
	eleventyConfig.addFilter("directoryPrefix", (inputPath) => {
		return getNumberPrefix(inputPath)[0];
	});

	eleventyConfig.addFilter("sortByDirectoryPrefix", (array) => {
		return array.sort((a, b) => {
			const [aBefore, aAfter] = getNumberPrefix(a.inputPath);
			const [bBefore, bAfter] = getNumberPrefix(b.inputPath);
			if (aBefore === bBefore) {
				return aAfter - bAfter;
			}
			return aBefore - bBefore;
		});
	});

	eleventyConfig.addFilter("sort", (array, key, ascending = true) => {
		if (ascending) {
			return array.sort((a, b) => {
				if (a.data[key] > b.data[key]) {
					return 1;
				}
				return -1;
			});
		} else {
			return array.sort((a, b) => {
				if (a.data[key] > b.data[key]) {
					return -1;
				}
				return 1;
			});
		}
	});
};
