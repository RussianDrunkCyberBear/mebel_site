$(document).ready(function() {

	$('.jqImgViewer-main-img-cont').click( function(event) {
		event.preventDefault();
	});
	
	$('.jqImgViewer-other-img-cont').click( function(event) {
		event.preventDefault();
		var clicked_img_url = $('img', this).attr('src');
		$('.jqImgViewer-other-img-cont').removeClass('jqImgViewer-selected-item');
		$(this).addClass('jqImgViewer-selected-item');
		$('.jqImgViewer-main-img-cont').attr('href', clicked_img_url);
		$('.jqImgViewer-main-img-cont > img').attr('src', clicked_img_url);
		// alert(clicked_img_url);
	});

	$('.jqImgViewer-arrow-left').click( function() {
		var prev_item = $(".jqImgViewer-selected-item").prev();
		if ($(".jqImgViewer-selected-item").is(':nth-child(2)')) {
			prev_item = $(".jqImgViewer-other-img-cont:last-child")
		};
		var prev_img_url = prev_item.children('img').attr('src');
		$('.jqImgViewer-other-img-cont').removeClass('jqImgViewer-selected-item');
		prev_item.addClass('jqImgViewer-selected-item');
		$('.jqImgViewer-main-img-cont').attr('href', prev_img_url);
		$('.jqImgViewer-main-img-cont > img').attr('src', prev_img_url);
	});

	$('.jqImgViewer-arrow-right').click( function() {
		var next_item = $(".jqImgViewer-selected-item").next();
		if ($(".jqImgViewer-selected-item").is(':last-child')) {
			next_item = $(".jqImgViewer-other-img-cont:nth-child(2)");
		};
		var next_img_url = next_item.children('img').attr('src');
		$('.jqImgViewer-other-img-cont').removeClass('jqImgViewer-selected-item');
		next_item.addClass('jqImgViewer-selected-item');
		$('.jqImgViewer-main-img-cont').attr('href', next_img_url);
		$('.jqImgViewer-main-img-cont > img').attr('src', next_img_url);
	});


});