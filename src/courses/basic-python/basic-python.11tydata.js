module.exports = {
	course_id: "basic-python",
	course_name: "Basic Python for Beginners",
	course_slug: "basic-python",
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
