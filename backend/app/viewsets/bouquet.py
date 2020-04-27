from rest_framework import viewsets

from app.models import BaseBouquet
from app.filters import BouquetFilter
from app.serializers.bouquet import BaseBouquetSerializer


class BouquetViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'options')
    queryset = BaseBouquet.objects.filter(is_active=True)
    serializer_class = BaseBouquetSerializer
    filter_class = BouquetFilter

