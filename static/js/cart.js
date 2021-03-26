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

    function addToCart(selector) {
        $.ajax({
            url: selector.attr('url'),
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                $('.header a.cart span').text(response.cart_total)
            },
        });
    }

    $('.btn-add-cart').on('click', function () {
       addToCart($(this));
    })
    $('.add-cart-detail').on('click', function () {
        addToCart($(this));
    })
});