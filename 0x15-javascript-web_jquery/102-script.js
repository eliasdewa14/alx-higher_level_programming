$(document).ready(function () {
	$("INPUT#btn_translate").click(function () {
		$.get(
			`https://fourtonfish.com/hellosalut/hello/?lang=${$("INPUT#language_code").val()}`,
			function (data) {
				$("div#hello").text(data.hello);
			}
		);
	});
});