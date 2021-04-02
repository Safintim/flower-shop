from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


class ConfigFilter:
    method = 'GET'
    layout_button = Submit('submit', 'Применить фильтр')
    column_classes = 'form-group col-md-4 mb-0'
    layout_title = Column('title', css_class=column_classes)
    layout_is_active = Column('is_active', css_class=column_classes)


class ListFormHelper(FormHelper):
    def __init__(self, form, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            Row(*[self.get_column(field) for field in form.fields.keys()]),
            Row(ConfigFilter.layout_button)
        )

        self.form_method = ConfigFilter.method

    def get_column(self, field):
        return Column(field, css_class=ConfigFilter.column_classes)


class ProductFilterFormHelper(FormHelper):
    form_method = ConfigFilter.method
    layout = Layout(
        Row(
            ConfigFilter.layout_title,
            Column('price_min', css_class=ConfigFilter.column_classes),
            Column('price_min', css_class=ConfigFilter.column_classes),
        ),
        Row(
            ConfigFilter.layout_is_active,
            Column('is_hit', css_class=ConfigFilter.column_classes),
            Column('is_new', css_class=ConfigFilter.column_classes),
        ),
        Row(
            Column('type', css_class=ConfigFilter.column_classes),
            Column('color', css_class=ConfigFilter.column_classes),
        ),
        Row(
            Column('categories', css_class=ConfigFilter.column_classes),
            Column('reasons', css_class=ConfigFilter.column_classes),
        ),
        Row(ConfigFilter.layout_button)
    )
