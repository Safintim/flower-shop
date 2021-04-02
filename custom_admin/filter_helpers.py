from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


class ConfigFilter:
    method = 'GET'
    layout_button = Submit('submit', 'Применить фильтр')
    column_classes = 'form-group col-md-4 mb-0'
    layout_title = Column('title', css_class=column_classes)
    layout_is_active = Column('is_active', css_class=column_classes)


class CategoryFilterFormHelper(FormHelper):
    form_method = ConfigFilter.method
    layout = Layout(
        Row(
            ConfigFilter.layout_title,
            Column('parent', css_class=ConfigFilter.column_classes),
            ConfigFilter.layout_is_active,
        ),
        Row(ConfigFilter.layout_button)
    )


class ReasonFilterFormHelper(FormHelper):
    form_method = ConfigFilter.method
    layout = Layout(
        Row(ConfigFilter.layout_title, ConfigFilter.layout_is_active),
        Row(ConfigFilter.layout_button)
    )


class ColorFilterFormHelper(ReasonFilterFormHelper):
    form_method = ConfigFilter.method
    layout = Layout(
        Row(ConfigFilter.layout_title, ConfigFilter.layout_is_active),
        Row(ConfigFilter.layout_button)
    )


class FlowerFilterFormHelper(FormHelper):
    form_method = ConfigFilter.method
    layout = Layout(
        Row(
            ConfigFilter.layout_title,
            Column('price_min', css_class=ConfigFilter.column_classes),
            Column('price_max', css_class=ConfigFilter.column_classes),
            ConfigFilter.layout_is_active,
            Column('is_add_filter', css_class=ConfigFilter.column_classes),
        ),
        Row(ConfigFilter.layout_button)
    )


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
