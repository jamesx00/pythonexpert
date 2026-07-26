const isMac = navigator.platform.toUpperCase().indexOf("MAC") >= 0;

if (isMac) {
	for (const el of document.getElementsByClassName("mac-key-label")) {
		el.textContent = el.dataset.macLabel;
	}
}

document.addEventListener("alpine:init", () => {
	Alpine.data("commandPalette", () => ({
		open: false,
		query: "",
		activeIndex: 0,
		items: [],

		init() {
			const dataEl = document.getElementById("command-palette-data");
			this.items = dataEl ? JSON.parse(dataEl.textContent || "[]") : [];
		},

		get contextualItems() {
			const items = [];
			const nav = document.getElementById("lesson-nav-data");
			if (!nav) return items;
			if (nav.dataset.nextUrl) {
				items.push({ category: "Lesson", title: "Next lesson", subtitle: nav.dataset.nextTitle, url: nav.dataset.nextUrl });
			}
			if (nav.dataset.previousUrl) {
				items.push({
					category: "Lesson",
					title: "Previous lesson",
					subtitle: nav.dataset.previousTitle,
					url: nav.dataset.previousUrl,
				});
			}
			return items;
		},

		get filteredItems() {
			const query = this.query.trim().toLowerCase();
			const all = [...this.contextualItems, ...this.items];
			const source = !query
				? all.slice(0, 30)
				: all
						.filter((item) =>
							`${item.title} ${item.subtitle || ""} ${item.category}`
								.toLowerCase()
								.includes(query)
						)
						.slice(0, 50);
			return source.map((item, index) => ({ ...item, index }));
		},

		get groupedItems() {
			const groups = [];
			for (const item of this.filteredItems) {
				let group = groups.find((g) => g.category === item.category);
				if (!group) {
					group = { category: item.category, items: [] };
					groups.push(group);
				}
				group.items.push(item);
			}
			return groups;
		},

		show() {
			this.open = true;
			this.query = "";
			this.activeIndex = 0;
			this.$nextTick(() => this.$refs.searchInput?.focus());
		},

		hide() {
			this.open = false;
		},

		toggle() {
			this.open ? this.hide() : this.show();
		},

		move(delta) {
			const count = this.filteredItems.length;
			if (count === 0) return;
			this.activeIndex = (this.activeIndex + delta + count) % count;
			this.$nextTick(() => {
				this.$refs.resultsList
					?.querySelector('[data-active="true"]')
					?.scrollIntoView({ block: "nearest" });
			});
		},

		selectActive() {
			const item = this.filteredItems.find((i) => i.index === this.activeIndex);
			if (item) window.location.href = item.url;
		},
	}));
});

function isTypingContext(target) {
	if (!target) return false;
	const tag = target.tagName ? target.tagName.toLowerCase() : "";
	if (tag === "input" || tag === "textarea" || tag === "select") return true;
	if (target.isContentEditable) return true;
	if (target.closest && target.closest(".monaco-editor")) return true;
	return false;
}

document.getElementById("command-palette-trigger")?.addEventListener("click", () => {
	window.dispatchEvent(new CustomEvent("toggle-command-palette"));
});

document.getElementById("shortcuts-help-trigger")?.addEventListener("click", () => {
	window.dispatchEvent(new CustomEvent("toggle-shortcuts-help"));
});

window.addEventListener(
	"keydown",
	(event) => {
		const key = event.key.toLowerCase();
		const cmdOrCtrl = isMac ? event.metaKey : event.ctrlKey;

		if (cmdOrCtrl && key === "k") {
			event.preventDefault();
			window.dispatchEvent(new CustomEvent("toggle-command-palette"));
			return;
		}

		if (isTypingContext(event.target)) return;

		if (event.key === "/") {
			event.preventDefault();
			window.dispatchEvent(new CustomEvent("open-command-palette"));
			return;
		}

		if (event.key === "?") {
			event.preventDefault();
			window.dispatchEvent(new CustomEvent("toggle-shortcuts-help"));
			return;
		}
	},
	true
);
