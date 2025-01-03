if (location.href.indexOf("#invite_token") != -1) {
	var urlSplit = document.URL.split("#");
	window.location = `/admin/#${urlSplit[1]}`;
}

// @ts-check
function getCookie(name) {
	const value = `; ${document.cookie}`;
	const parts = value.split(`; ${name}=`);
	if (parts.length === 2) return parts.pop().split(";").shift();
}

function getLanguageFromCookie() {
	return getCookie("preferred_language");
}

/**
 * Get the language from the cookie or the browser
 * @returns {string}
 */
function getUserLanguage() {
	const userLang = navigator.language || navigator.userLanguage;
	const fullSelectedLanguage = getLanguageFromCookie() || userLang;
	const selectedLanguage = fullSelectedLanguage.split("-")[0];
	return selectedLanguage;
}

function addCopyBlock() {
	const codeBlocks = document.querySelectorAll(".prose pre code");

	for (const codeBlock of codeBlocks) {
		const alreadyHasCopyIcon =
			codeBlock.getElementsByClassName("copy-content").length > 0;

		if (alreadyHasCopyIcon) continue;

		const copyIcon = document.createElement("div");
		copyIcon.classList.add("copy-content");
		copyIcon.classList.add("text-sm");
		copyIcon.innerHTML = '<i class="far fa-fw fa-copy"></i>';

		copyIcon.addEventListener("click", async (e) => {
			const target = e.currentTarget;
			const textToCopy = target.closest("code").textContent.trim();
			await navigator.clipboard.writeText(textToCopy);
			target.innerHTML = '<i class="fas fa-fw fa-check"></i>';
			setTimeout(() => {
				target.innerHTML = '<i class="far fa-fw fa-copy"></i>';
			}, 1000);
		});

		codeBlock.appendChild(copyIcon);
	}
}
