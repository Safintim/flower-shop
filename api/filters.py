from django_filters import rest_framework as filters

from main.models import Product


class NumberFilterInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class ProductFilter(filters.FilterSet):
    categories = NumberFilterInFilter(field_name='categories__pk', lookup_expr='in', label='Категории')
    reasons = NumberFilterInFilter(field_name='reasons__pk', lookup_expr='in', label='Поводы')
    price = filters.RangeFilter(field_name='price')

    class Meta:
        model = Product
        fields = ('categories', 'color', 'reasons', 'price')
