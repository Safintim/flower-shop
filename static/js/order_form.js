$(function () {
    $('#id_postcard_1').on('change', function () {
        if ($(this).is(':checked')) {
            $('.postcard_text').attr('hidden', false)
        }
    })
    $('#id_postcard_2').on('change', function () {
        if ($(this).is(':checked')) {
            $('.postcard_text').attr('hidden', true)
        }
    })


    $('#id_recipient_1').on('change', function () {
        if ($(this).is(':checked')) {
            $('.recipient_info').attr('hidden', true)
            $('.recipient_call').attr('hidden', true)
        }
    })
    $('#id_recipient_2').on('change', function () {
        if ($(this).is(':checked')) {
            $('.recipient_info').attr('hidden', false)

            $('.recipient_call').attr('hidden', false)
        }
    })


    $('#id_recipient_call_1').on('change', function () {
        if ($(this).is(':checked')) {
            $('.delivery_info').attr('hidden', false)
        }
    })
    $('#id_recipient_call_2').on('change', function () {
        if ($(this).is(':checked')) {
            $('.delivery_info').attr('hidden', true)
        }
    })


    $('#id_delivery_type_1').on('change', function () {
        if ($(this).is(':checked')) {
            $('.recipient_call').attr('hidden', false)
            $('.delivery_info').attr('hidden', false)

        }
    })
    $('#id_delivery_type_2').on('change', function () {
        if ($(this).is(':checked')) {
            $('.recipient_call').attr('hidden', true)
            $('.delivery_info').attr('hidden', true)
        }
    })
});