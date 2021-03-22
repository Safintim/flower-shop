$(function () {
    $('.cart-product-delete').on('click', function () {
        var a = $(this)
        $.ajax({
            url: $(this).attr('url'),
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
                const pk = a.attr('pk');
                const css_class = `#cart-product-${pk}`
                $(css_class).remove()
            },
        });
    })
});