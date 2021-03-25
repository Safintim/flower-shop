from crispy_forms.bootstrap import InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit
from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'postcard',
            'postcard_text',
            'delivery_type',
            'delivery_date',
            'recipient',
            'recipient_name',
            'recipient_phone',
            'recipient_call',
            'recipient_address',
            'delivery_time',
            'comment',
        )
        widgets = {
            'postcard': forms.RadioSelect(),
            'postcard_text': forms.Textarea(attrs={'rows': 5}),
            'delivery_type': forms.RadioSelect(),
            'delivery_date': forms.TextInput(attrs={'type': 'date'}),
            'delivery_time': forms.TextInput(attrs={'type': 'time'}),
            'recipient': forms.RadioSelect(),
            'recipient_call': forms.RadioSelect(),
            'comment': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(InlineRadios('postcard'), css_class='row my-2'),
            Div(Field('postcard_text'), hidden='true', css_class='row my-2 postcard_text'),
            Div(InlineRadios('delivery_type'), css_class='row my-2'),
            Div('delivery_date', css_class='row my-2'),
            Div(InlineRadios('recipient'), css_class='row my-2'),
            Div(
                Div('recipient_name', css_class='mr-3 recipient_info', hidden='true'),
                Div('recipient_phone', css_class='recipient_info', hidden='true'),
                css_class='row my-2'
            ),
            Div(InlineRadios('recipient_call'), css_class='row my-2 recipient_call', hidden='true'),
            Div(
                Div('recipient_address', css_class='mr-3 delivery_info', hidden='true'),
                Div('delivery_time', css_class='delivery_info', hidden='true'),
                css_class='row my-2'
            ),
            Div('comment', css_class='row my-2'),
            Div(Submit('submit', 'Заказать', css_class='btn orange-btn'), css_class='row my-2')
        )
        self.helper.form_method = 'post'
        self.helper.form_action = 'order-create'
        self.helper.form_class = 'order-form'
        self.helper.label_class = 'label'


class OrderCheckStatusForm(forms.Form):
    pk = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.helper.form_action = 'order-check-status'
        self.helper.layout = Layout(
            'pk',
            Submit('submit', 'Проверить', css_class='btn orange-btn')
        )

    def clean_pk(self):
        pk = self.cleaned_data.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if not order:
            self.add_error('pk', 'Заказ с данным номером не найден')
        return pk
