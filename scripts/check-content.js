#!/usr/bin/env node
// Usage: npm run check-content [-- <courses dir>]
const path = require("path");
const { checkCourses } = require("./content-checker");

async function main() {
	const coursesDir = path.resolve(
		process.argv[2] || path.join(__dirname, "..", "src", "courses")
	);
	const report = await checkCourses(coursesDir);
	for (const error of report.errors) {
		const where =
			error.testId === undefined
				? error.lesson
				: `${error.lesson} (test ${error.testId})`;
		console.error(`✗ ${where}: ${error.message}`);
	}
	console.log(
		`Checked ${report.lessonsChecked} lessons: ${report.errors.length} problem(s).`
	);
	process.exitCode = report.errors.length > 0 ? 1 : 0;
}

main().catch((error) => {
	console.error(error);
	process.exitCode = 1;
});
