module.exports = {
	layout: "layouts/lesson.njk",
	tags: ["lesson"], // This is set so that all subdirectories are tagged as lesson
	eleventyComputed: {
		title: (data) => {
			if (data.tags.indexOf("lesson") !== -1) {
				return `${data.lesson_name} - ${data.course_name}`;
			} else {
				return data.title;
			}
		},
	},
};
