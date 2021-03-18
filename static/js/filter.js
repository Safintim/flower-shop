$(function () {
    const URL = $('form.filter').attr('action');
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
            url: URL,
            data: {
                price__lte: $('#price_max').val(),
                price__gte: $('#price_min').val(),
            },
            success: function (response) {
                $('#product-list').html(response)
            }
        })
    })
    $('.filter :checkbox').on('change', function () {

        let reasonIds = $(".filter input[type=checkbox]:checked").map(function () {
            return $(this).val();
        }).get();
        let query = reasonIds.map(function (el) {
            return `reasons=${el}`
        }).join('&')
        let url = `${URL}?${query}`
        $.ajax({
            type: 'GET',
            url: url,
            success: function (response) {
                $('#product-list').html(response)
            }
        })
    })

});
