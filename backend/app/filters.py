import rest_framework_filters as filters

from app.models import BaseBouquet, Category, Reason


class NumberRangeFilter(filters.BaseRangeFilter, filters.NumberFilter):
    pass


class BouquetFilter(filters.FilterSet):
    color = filters.CharFilter(
        field_name='color', lookup_expr='iexact', label='Цвет',
    )
    category = filters.ModelChoiceFilter(queryset=Category.objects.all())
    reason = filters.ModelChoiceFilter(queryset=Reason.objects.all())
    price = NumberRangeFilter(method='filter_by_price', label='Цена')

    def filter_by_price(self, qs, name, value):
        min, max = value
        base_ids = set()
        for base in qs:
            for bouquet in base.bouquets.all():
                if min <= bouquet.bouquet_price() <= max:
                    base_ids.add(base.id)
        return BaseBouquet.objects.filter(id__in=base_ids)

    class Meta:
        models = BaseBouquet
        exclude = ('id', )
