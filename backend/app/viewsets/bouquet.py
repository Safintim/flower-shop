from rest_framework import viewsets

from app.models import BaseBouquet
from app.filters import BouquetFilter
from app.serializers.bouquet import (
    BaseBouquetDetailSerializer,
    BaseBouquetListSerializer
)


class BouquetViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'options')
    queryset = BaseBouquet.objects.filter(is_active=True)
    serializer_class = BaseBouquetListSerializer
    filter_class = BouquetFilter
    serializer_action_class = {
        'retrieve': BaseBouquetDetailSerializer
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_class[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def get_queryset(self):
        return super().get_queryset().distinct()

    def list(self, request, *args, **kwargs):
        print(request.query_params)
        return super().list(request, *args, **kwargs)
