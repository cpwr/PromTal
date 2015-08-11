;(function ($, window, document, undefined) {

    var pluginName = "metisMenu",
        defaults = {
            toggle: true
        };
        
    function Plugin(element, options) {
        this.element = element;
        this.settings = $.extend({}, defaults, options);
        this._defaults = defaults;
        this._name = pluginName;
        this.init();
    }

    Plugin.prototype = {
        init: function () {

            var $this = $(this.element),
                $toggle = this.settings.toggle;

            $this.find('li.active').has('ul').children('ul').addClass('collapse in');
            $this.find('li').not('.active').has('ul').children('ul').addClass('collapse');
            $this.find('li').has('ul').children('a').on('click', function (e) {
                e.preventDefault();
                if ($(this).children('span').hasClass('fa-plus-square-o')) {
                    $(this).children('span').removeClass('fa-plus-square-o').addClass('fa-minus-square-o');
                } else {
                    $(this).children('span').removeClass('fa-minus-square-o').addClass('fa-plus-square-o');
                }
                $(this).parent('li').toggleClass('active').children('ul').collapse('toggle');
                console.log("qqqqqqqqqq3");
                if ($toggle) {
                    $(this).parent('li').siblings().removeClass('active').children('ul.in').collapse('hide');
                    //$(this).children('span').removeClass('fa-minus-square-o');
                }
            });
        }
    };

    $.fn[ pluginName ] = function (options) {
        return this.each(function () {
            if (!$.data(this, "plugin_" + pluginName)) {
                $.data(this, "plugin_" + pluginName, new Plugin(this, options));
            }
        });
    };

})(jQuery, window, document);
