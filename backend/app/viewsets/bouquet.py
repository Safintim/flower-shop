from rest_framework import viewsets

from app.models import BaseBouquet
from app.serializers.bouquet import BouquetSerializer


class BouquetViewSet(viewsets.ModelViewSet):
    http_method_names = ['options', 'get']
    serializer_class = BouquetSerializer

    def get_queryset(self):
        return BaseBouquet.objects.filter(is_active=True)
