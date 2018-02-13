    $(document).ready(function() {
    
        $('.arrow-left').click( function() {
            var cur_margin_lft = parseFloat($('.slide-content').css("margin-left"));
            var element_width = parseFloat($('.slider-element').css("width")) + parseFloat($('.slider-element').css("margin-left"));
            cur_margin_lft = cur_margin_lft + element_width;
            if (cur_margin_lft > 0) {
                cur_margin_lft = 0;
            }
            cur_margin_lft = cur_margin_lft + "px";
            $('.slide-content').animate({"margin-left":cur_margin_lft}, 300);
        });
        
        $('.arrow-right').click( function() {
            var cur_margin_lft = parseFloat($('.slide-content').css("margin-left"));
            var element_width = parseFloat($('.slider-element').css("width")) + parseFloat($('.slider-element').css("margin-left"));
            var slider_frame_width = parseFloat($('.slider-frame').css("width"));
            var elements_cnt = $('.slider-element').length;
            var all_elements_width = element_width * elements_cnt + parseFloat($('.slider-element').css("margin-left"));
            cur_margin_lft = cur_margin_lft - element_width;
            if ((cur_margin_lft) < (slider_frame_width - all_elements_width)) {
                cur_margin_lft = slider_frame_width - all_elements_width;
            }
            cur_margin_lft = cur_margin_lft + "px";
            $('.slide-content').animate({"margin-left":cur_margin_lft}, 300);

        });
    });
