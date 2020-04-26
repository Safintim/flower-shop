from rest_framework import viewsets

from app.models import BaseBouquet
from app.serializers.bouquet import BaseBouquetSerializer


class BouquetViewSet(viewsets.ModelViewSet):
    http_method_names = ['options', 'get']
    serializer_class = BaseBouquetSerializer

    def get_queryset(self):
        return BaseBouquet.objects.filter(is_active=True)
