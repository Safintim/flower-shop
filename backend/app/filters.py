import rest_framework_filters as filters
from django.db.models import Q

from app.models import BaseBouquet, Category, Reason, Flower, Product


class NumberRangeFilter(filters.BaseRangeFilter, filters.NumberFilter):
    pass


class ChoicesInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class FlowerFilter(filters.FilterSet):
    class Meta:
        model = Flower
        fields = {
            'id': ['in'],
        }


class ProductFilter(filters.FilterSet):
    flowers = filters.RelatedFilter(
        FlowerFilter,
        field_name='flowers',
        queryset=Flower.objects.all(),
    )

    class Meta:
        model = Product
        fields = ('id',)


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = {'id': ['in']}


class BouquetFilter(filters.FilterSet):
    color = ChoicesInFilter(
        field_name='color',
        lookup_expr='in',
        label='Цвет',
    )
    is_show_on_main_page = filters.BooleanFilter(
        field_name='is_show_on_main_page',
        label='Показать на главной странице',
    )
    category = filters.RelatedFilter(
        CategoryFilter,
        field_name='category',
        queryset=Category.objects.all(),
        distinct=True,
    )
    bouquets = filters.RelatedFilter(
        ProductFilter,
        field_name='bouquets',
        queryset=Product.objects.all(),
    )
    reason = filters.ModelMultipleChoiceFilter(queryset=Reason.objects.all())
    price = NumberRangeFilter(method='filter_by_price', label='Цена')
    search = filters.CharFilter(
        method='filter_by_title',
        field_name='title',
        label='Поиск',
    )

    def filter_by_price(self, qs, name, value):
        min, max = value
        base_ids = set()
        for base in qs:
            for bouquet in base.bouquets.all():
                if min <= bouquet.bouquet_price() <= max:
                    base_ids.add(base.id)
                    break
        return BaseBouquet.objects.filter(id__in=base_ids)

    def filter_by_title(self, qs, name, value):
        qs = qs.filter(
            Q(title__icontains=value)
            | Q(bouquets__flowers__title__icontains=value),
        )
        return qs

    class Meta:
        models = BaseBouquet
        exclude = ('id',)
