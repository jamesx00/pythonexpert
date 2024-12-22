require("dotenv").config();

module.exports = {
	...process.env,
	base_url:
		process.env.DEVELOPMENT === "true"
			? "http://localhost:8080"
			: "https://www.pythonexpert.dev",
};
