$(document).ready(function () {
	$("INPUT#btn_translate").click(translate);
	$("INPUT#language_code").keyup(function (evt) {
		if (evt.keyCode === 13) {
			translate();
		}
	});

	function translate() {
		$.get(
			`https://fourtonfish.com/hellosalut/hello/?lang=${$("INPUT#language_code").val()}`,
			function (data) {
				$("#hello").text(data.hello);
			}
		);
	}
});