import django_filters

from main.models import Category, Reason, Color, Flower


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


class FlowerFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Flower
        fields = ('title', 'price_min', 'price_max', 'is_active', 'is_add_filter')
