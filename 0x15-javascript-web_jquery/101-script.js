$(document).ready(function () {
	$("div#add_item").click(function () {
		$("<li>").text("Item").appendTo("ul.my_list");
	});
	$("div#remove_item").click(function () {
		$("ul.my_list li:last-child").remove();
	});
	$("div#clear_list").click(function () {
		$("ul.my_list").empty();
	});
});