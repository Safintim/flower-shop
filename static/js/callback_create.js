$(document).ready(function () {
    $('#callback-btn').click(function () {
        const errorText = 'Неправильный формат телефона. Попробуйте снова'
        $.ajax({
            url: '{% url "callback-create" %}',
            type: 'POST',
            data: {
                phone: $('#callback-input').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (json) {
                if (json.status === 'error') {
                    $('#callbackOkModalLabel').text(errorText)
                }
            },
            error: function () {
                $('#callbackOkModalLabel').text(errorText)
            }
        });

    });
});