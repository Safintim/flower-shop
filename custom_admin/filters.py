import django_filters

from main.models import Category, Reason, Color


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
