/**
 * 轮播图
 * gjj 2018年4月13日 whellote@163.com
 *
 */
(function(){

    var xSlider = function(el, userConfig) {
        var _this = this;
        this.el = el;

        // 参数配置 ----轮播图配置(默认参数)
        default_config = {
            w: this.el.width(),
            current: 0,
            speed: 500,
            intervalTime: 5000
        }

        // 合并更新最终 config
        if (userConfig != null) {
            this.config = $.extend(default_config, userConfig);
        } else {

        }


        // 保存查找dom 元素
        var slider_img = this.el.children('.slider-img');	// 图片div, 页面结构为div -> ul -> li -> img
        var slider_img_ul = slider_img.children('ul')
        var slider_img_ul_li = slider_img_ul.children('li')
        var picNum = slider_img_ul_li.length;

        // 初始化左右按钮
        var left_style = '<a href="javascript:" class="slider-btn slider-btn-left">&lt;</a>';
        var right_style = '<a href="javascript:" class="slider-btn slider-btn-right">&gt;</a>';

        this.el.append(left_style);
        this.el.append(right_style);

        var slider_btn_left = this.el.children('.slider-btn-left');
        var slider_btn_right = this.el.children('.slider-btn-right')

        // 初始化圆点
        var dot_list_style = '<div class="slider-dot"><ul></ul></div>';
        this.el.append(dot_list_style);

        var slider_dot = this.el.children('.slider-dot');
        var slider_dot_ul = slider_dot.children('ul');

        // 根据从html中获取的图片数生成圆点
        for (var i = 0; i < picNum; i++) {
            slider_dot_ul.append('<li></li>');
        }

        var slider_dot_ul_li = slider_dot_ul.children('li');
        active(this.config.current);    // 初始化选中



        // 初始化默认显示图片位置
        slider_img_ul.css('left', 0);

        // 左右按钮点击切换
        slider_btn_right.on('click', function() {
            event.preventDefault();
            toggleInterval ()
            toPage(getNext(_this.config.current));
            currentPlus();
        });
        slider_btn_left.on('click', function() {
            event.preventDefault();
            toggleInterval ()
            toPage(getPre(_this.config.current));
            currentMinus();
        });

        // 圆点切换点亮
        function active(index) {
            slider_dot_ul_li.removeClass('active');
            slider_dot_ul_li.eq(index).addClass('active');
        }


        // 点击圆点切换
        slider_dot_ul_li.on('click', function(event) {
            event.preventDefault();
            toggleInterval();
            var index = $(this).index();
            active(index);
            toPage(index);
            _this.config.current = index;
        });


        // 自动切换
        var sliderInt = setInterval(sliderInterval, _this.config.intervalTime);

        // 执行轮播
        function sliderInterval() {
            // console.log('current: ' + _this.config.current + '----- next: ' + getNext(_this.config.current));
            toPage(getNext(_this.config.current));
            currentPlus();

        }

        // 重置计时器
        function toggleInterval () {
            clearInterval(sliderInt);
            sliderInt = setInterval(sliderInterval, _this.config.intervalTime);
        }

        // TEST
        // toPage(4)
        // getNext(4)
        // getNext(0);
        // active(1)


        // 当前页加一
        function currentPlus() {
            if (_this.config.current < picNum - 1){
                _this.config.current ++;
            } else {
                _this.config.current = 0;
            }
        }

        // 当前页减一
        function currentMinus() {
            if (_this.config.current === 0) {
                _this.config.current = picNum - 1;
            } else {
                _this.config.current --;
            }
        }

        // 获取下一页的页码
        function getNext(index) {
            var next;
            if (index < picNum - 1) {
                next = index + 1;
            }
            if (index === picNum - 1 ) {
                next = 0;
            }

            // console.log('next: ' + next);

            return next;
        }

        // 获取上一页的页码
        function getPre(index) {
            var pre;
            if (index === 0) {
                pre = picNum - 1;
            }

            if (index > 0) {
                pre = index - 1;
            }

            return pre;
        }

        // 翻到index页
        function toPage(index) {
            slider_img_ul.stop(true, false).animate({left: - _this.config.w * index}, this.config.speed, function(){
                // 更新圆点
                active(index);
            });
        }



    }

    // 将xSlider 方法合并到选择器选取的元素中
    $.fn.extend({
        xSlider: function(config) {
            new xSlider($(this), config)
        }
    })


})();

var config = {
    current: 0,
    speed: 500,
    intervalTime: 5000
}

$('.slider').xSlider(config);