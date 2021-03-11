$(function () {
    $('#slider').slider({
        range: true,
        min: 0,
        max: 9999,
        values: ['1000', '9000'],
        slide: function (event, ui) {
            $('#price_min').val(ui.values[0]);
            $('#price_max').val(ui.values[1]);
        }
    });
    $('#btn_price').on('click', function () {
        $.ajax({
            type: 'GET',
            url: $('form.filter').attr('action'),
            data: {
                price__lte: $('#price_max').val(),
                price__gte: $('#price_min').val(),
            },
            success: function (response) {
                $('#product-list').html(response)
            }
        })
    })
});
