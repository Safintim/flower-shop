$(function () {
    $('.dropdown-toggle').on('click', function (e) {
        $(this).next().toggle();
    });
    $('.dropdown-menu.keep-open').on('click', function (e) {
        e.stopPropagation();
    });
    if (1) {
        $('body').attr('tabindex', '0');
    } else {
        alertify.confirm().set({'reverseButtons': true});
        alertify.prompt().set({'reverseButtons': true});
    }
});