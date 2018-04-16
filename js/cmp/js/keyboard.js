$(function () {

    var e_username = $("#username"),
        e_pwd = $("#password"),
        shift = false,
        capslock = false,
        input_element_id = null;

    function saveBlurInputId(){

        setTimeout(function(){
            var current_focus_id = document.activeElement.id;
            // console.log('current_focus_id');
            // console.log(current_focus_id);
            if (current_focus_id && current_focus_id.toUpperCase() == 'USERNAME' || current_focus_id.toUpperCase() == 'PASSWORD'){
                input_element_id = current_focus_id;
            }

            // console.log(input_element_id)
        }, 0);


    }

    $('.login').delegate("*", "focus blur", function (e) {
        saveBlurInputId();
    });

    // e_username.focus(function() {
    //     saveBlurInputId();
    // });
    //
    // e_pwd.focus(function () {
    //     saveBlurInputId();
    // });
    //
    // e_username.blur(function () {
    //     saveBlurInputId();
    // });
    // e_pwd.blur(function () {
    //     saveBlurInputId();
    // });

    $('#keyboard li').click(function () {
        saveBlurInputId()
        var $this = $(this);
        var character = $this.html();

        var e_focus_jq = $('#' + input_element_id);
        var html = e_focus_jq.val();

        // console.log('character: ');
        // console.log(character);

        //  shift
        if ($this.hasClass('left-shift') || $this.hasClass('right-shift')) {
            $('.letter').toggleClass('uppercase');
            $('.symbol span').toggle();

            shift = (shift === true) ? false : true;
            capslock = false;
            return false;
        }

        // Caps lock
        if ($this.hasClass('capslock')) {
            $('.letter').toggleClass('uppercase');
            capslock = true;
            return false;
        }

        // Delete
        if ($this.hasClass('delete')) {
            e_focus_jq.val(html.substr(0, html.length - 1));
            return false;
        }

        // special characters
        // 标点
        if ($this.hasClass('symbol')) {
            // console.log('symbol');
            // console.log($('span:visible', $this));
            character = $('span:visible', $this).html();
        }

        // 空格
        if ($this.hasClass('space')) {
            character = " ";
        }

        // 制表符
        if ($this.hasClass('tab')) {
            character = "\t";
        }

        // 回车
        if ($this.hasClass('return')) {
            character = "\n";
        }


        // 大写字母
        if ($this.hasClass('uppercase')) {
            character = character.toUpperCase();
        }

        // shift还原

        if (shift === true) {
            $('.symbol span').toggle();
            if (capslock === false) {
                $('.letter').toggleClass('uppercase');
            }

            shift = false;
        }

        // 回写到文本框
        e_focus_jq.val(e_focus_jq.val() + character);
    });


});
