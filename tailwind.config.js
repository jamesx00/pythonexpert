/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		"src/**/*.{html,md,njk,js}",
		"_includes/**/*.{html,md,njk,js}",
		"!public/js/monaco-editor/**/*.js",
		"!public/js/pe-monaco-editor.js",
		"public/js/**/*.js",
		"builds/**/*.js",
	],
	theme: {
		extend: {
			colors: {
				// terminal accent blue, brightest at 900 for legibility on dark backgrounds
				primary: {
					50: "#003E6B",
					100: "#0A558C",
					200: "#0F609B",
					300: "#186FAF",
					400: "#2680C2",
					500: "#4098D7",
					600: "#62B0E8",
					700: "#84C5F4",
					800: "#B6E0FE",
					900: "#DCEEFB",
				},
				// terminal green accent, used for success/prompt states
				secondary: {
					50: "#1E3A1E",
					100: "#2A4F2A",
					200: "#356334",
					300: "#3F7A3D",
					400: "#4E9A49",
					500: "#5FBD58",
					600: "#7FD177",
					700: "#A0E098",
					800: "#C4EEBE",
					900: "#E4F9E0",
				},
				// cool terminal grey scale (dark surfaces + muted foreground text)
				neutral: {
					50: "#F4F6FB",
					100: "#E4E8F1",
					200: "#C9CFDE",
					300: "#A6ADC8",
					400: "#8B92B0",
					500: "#6C7293",
					600: "#4E5372",
					700: "#383C55",
					800: "#22243A",
					900: "#14151F",
				},
				term: {
					bg: "#12131c",
					surface: "#1a1c2a",
					raised: "#22243a",
					border: "#33364d",
					text: "#d9dcf2",
					muted: "#8b92b0",
					accent: "#89b4fa",
					green: "#a6e3a1",
					yellow: "#f9e2af",
					red: "#f38ba8",
					pink: "#f5c2e7",
				},
			},
		},
		fontFamily: {
			"victor-mono": ["Victor Mono", "ui-monospace", "SFMono-Regular", "Menlo", "Consolas", "monospace"],
			mono: ["Victor Mono", "ui-monospace", "SFMono-Regular", "Menlo", "Consolas", "monospace"],
		},
	},
	darkMode: "class",
	plugins: [require("@tailwindcss/typography")],
};
