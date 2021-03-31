from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


class ConfigFilter:
    method = 'GET'
    button = Submit('submit', 'Применить фильтр')


class CategoryFilterFormHelper(FormHelper):
    form_method = ConfigFilter.method
    column_classes = 'form-group col-md-4 mb-0'
    layout = Layout(
        Row(
            Column('title', css_class=column_classes),
            Column('parent', css_class=column_classes),
            Column('is_active', css_class=column_classes),
        ),
        Row(ConfigFilter.button)
    )


class ReasonFilterFormHelper(FormHelper):
    form_method = ConfigFilter.method
    column_classes = 'form-group col-md-6 mb-0'
    layout = Layout(
        Row(
            Column('title', css_class=column_classes),
            Column('is_active', css_class=column_classes),
        ),
        Row(ConfigFilter.button)
    )


class ColorFilterFormHelper(ReasonFilterFormHelper):
    form_method = ConfigFilter.method
    column_classes = 'form-group col-md-6 mb-0'
    layout = Layout(
        Row(
            Column('title', css_class=column_classes),
            Column('is_active', css_class=column_classes),
        ),
        Row(ConfigFilter.button)
    )


class FlowerFilterFormHelper(FormHelper):
    form_method = ConfigFilter.method
    column_classes = 'form-group col-md-4 mb-0'
    layout = Layout(
        Row(
            Column('title', css_class=column_classes),
            Column('price_min', css_class=column_classes),
            Column('price_max', css_class=column_classes),
            Column('is_active', css_class=column_classes),
            Column('is_add_filter', css_class=column_classes),
        ),
        Row(ConfigFilter.button)
    )


class ProductFilterFormHelper(FormHelper):
    form_method = ConfigFilter.method
    column_classes = 'form-group col-md-4 mb-0'
    layout = Layout(
        Row(
            Column('title', css_class=column_classes),
            Column('price_min', css_class=column_classes),
            Column('price_max', css_class=column_classes),
        ),
        Row(
            Column('is_active', css_class=column_classes),
            Column('is_hit', css_class=column_classes),
            Column('is_new', css_class=column_classes),
        ),
        Row(
            Column('type', css_class=column_classes),
            Column('color', css_class=column_classes),
        ),
        Row(
            Column('categories', css_class=column_classes),
            Column('reasons', css_class=column_classes),
        ),
        Row(ConfigFilter.button)
    )
