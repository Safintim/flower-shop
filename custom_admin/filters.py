import django_filters

from main.models import Category, Reason, Color, Flower, Product
from reviews.models import Review


class ConfigFilter:
    common_fields = ('is_active', 'title')


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ConfigFilter.common_fields + ('parent',)


class ReasonFilter(django_filters.FilterSet):
    class Meta:
        model = Reason
        fields = ConfigFilter.common_fields


class ColorFilter(ReasonFilter):
    class Meta(ReasonFilter.Meta):
        model = Color


class ReviewFilter(django_filters.FilterSet):
    class Meta:
        model = Review
        fields = ('name', 'is_active', )


class FlowerFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Flower
        fields = ConfigFilter.common_fields + ('price_min', 'price_max', 'is_add_filter')


class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ConfigFilter.common_fields + (
            'price_min',
            'price_max',
            'is_hit',
            'is_new',
            'type',
            'categories',
            'reasons',
            'color',
        )
