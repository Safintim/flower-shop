import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.urls import reverse_lazy

from main.models import Category, Reason, Color


class ConfigFilter:
    method = 'GET'
    button = Submit('submit', 'Применить фильтр')


class CategoryFilterFormHelper(FormHelper):
    form_method = ConfigFilter.method
    form_action = reverse_lazy('custom_admin:category-list')
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
    form_action = reverse_lazy('custom_admin:reason-list')
    column_classes = 'form-group col-md-6 mb-0'
    layout = Layout(
        Row(
            Column('title', css_class=column_classes),
            Column('is_active', css_class=column_classes),
        ),
        Row(ConfigFilter.button)
    )


ColorFilterFormHelper = ReasonFilterFormHelper


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ('title', 'parent', 'is_active',)


class ReasonFilter(django_filters.FilterSet):
    class Meta:
        model = Reason
        fields = ('title', 'is_active',)


class ColorFilter(ReasonFilter):
    class Meta(ReasonFilter.Meta):
        model = Color
