from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('phone', 'first_name', 'last_name', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            Div(Submit('submit', 'Войти', css_class='btn orange-btn'), css_class='text-center')
        )
        self.helper.form_method = 'post'
        self.helper.form_action = 'user-login'
