$(document).ready(function () {
	/* Prevent error in search function while searching on multible items */
	$('#advanced_search').submit(function () {
		if ($("#search_field option:selected").length>1) {
			$("#search_field option[value='']").removeAttr('selected');
		}
	})

	window.wrapper = $("#wrapper");

	/* init */
	animate_header();
});

/* Slide header background */
function animate_header() {
	window.wrapper.animate({'backgroundPosition':"1000px 0px"},10000)
			.animate({'backgroundPosition':"0px 0px"},10000,function () {animate_header()});
}
