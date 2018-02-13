 $(document).ready(function() {

        var timer = setTimeout(next_active_elem, 5000);
        
        // setTimeout(next_active_elem, 5000);

        change_element();

        $('.jqImgSlideBanner-menu-elem').mouseover( function() {
            if (!$(this).hasClass('jqImgSlideBanner-menu-elem-active')) {
                $('.jqImgSlideBanner-menu-elem').removeClass('jqImgSlideBanner-menu-elem-active');
                $(this).addClass('jqImgSlideBanner-menu-elem-active');
                change_element();
                clearTimeout(timer);
                timer = setTimeout(next_active_elem, 10000);
            };
        });

        function next_active_elem() {
            var next_active = $('.jqImgSlideBanner-menu-elem-active').next();
            if (!next_active.length) {
                next_active = $('.jqImgSlideBanner-menu-elem').first();
            };
            // alert( next_active.html())
            $('.jqImgSlideBanner-menu-elem').removeClass('jqImgSlideBanner-menu-elem-active');
            next_active.addClass('jqImgSlideBanner-menu-elem-active');
            change_element();
            timer = setTimeout(next_active_elem, 5000);
        };

        function change_element() {
            var banner_title = $('.jqImgSlideBanner-menu-elem-active > .jqImgSlideBanner-element-title-hidden').html();
            var banner_title_href = $('.jqImgSlideBanner-menu-elem-active > .jqImgSlideBanner-element-title-hidden').attr('href');
            $('.jqImgSlideBanner-element-title').css("opacity","0");
            $('.jqImgSlideBanner-element-title').html(banner_title);
            $('.jqImgSlideBanner-element-title').attr('href', banner_title_href);
             $('.jqImgSlideBanner-element-title').animate({"opacity":"1"}, 300);
            var banner_desription = $('.jqImgSlideBanner-menu-elem-active > .jqImgSlideBanner-element-descript-hidden').html();
            $('.jqImgSlideBanner-element-descript').css("opacity","0");
            $('.jqImgSlideBanner-element-descript').html(banner_desription);
            $('.jqImgSlideBanner-element-descript').animate({"opacity":"1"}, 500);
            $('.jqImgSlideBanner-element-descript a').attr('href', banner_title_href);
            var banner_img_old = $('.jqImgSlideBanner-element > img').last().attr('src');
            var banner_img = $('.jqImgSlideBanner-menu-elem-active > .jqImgSlideBanner-element-img-hidden').attr("src");
            $('.jqImgSlideBanner-element > img').first().attr('src', banner_img_old);
            $('.jqImgSlideBanner-element > img').last().attr('src', banner_img);
            $('.jqImgSlideBanner-element > img').last().css("opacity","0");
            $('.jqImgSlideBanner-element > img').last().animate({"opacity":"1"}, 300);
            $('.jqImgSlideBanner-line1, .jqImgSlideBanner-line2, .jqImgSlideBanner-line3').css("opacity","0");
            $('.jqImgSlideBanner-line1, .jqImgSlideBanner-line2, .jqImgSlideBanner-line3').animate({"opacity":"1"}, 500);
            $('.jqImgSlideBanner-line4').css("right","-20%");
            $('.jqImgSlideBanner-line4').animate({"right":"0"}, 300);
        };

});