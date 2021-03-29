from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from django import forms

from reviews.models import Review


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'phone', 'city', 'social_link', 'text', 'image')
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            *self.Meta.fields,
            Div(Submit('submit', 'Оставить отзыв', css_class='btn orange-btn'), css_class='text-center')
        )
        self.helper.form_method = 'post'
        self.helper.form_action = 'review-create'
