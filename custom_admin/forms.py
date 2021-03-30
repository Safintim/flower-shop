from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML


class CreateUpdateFormHelper(FormHelper):
    def __init__(self, create_update_action, delete_action=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'POST'
        self.form_action = create_update_action

        html = f'<a class="btn btn-danger" href="{delete_action}">Удалить</a>' if delete_action else ''
        self.layout = Layout(
            *self.layout.fields,
            Submit('save', 'Сохранить'),
            HTML(html)
        )
