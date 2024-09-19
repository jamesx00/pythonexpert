if (location.href.indexOf("#invite_token") != -1) {
	var urlSplit = document.URL.split("#");
	window.location = `/admin/#${urlSplit[1]}`;
}
