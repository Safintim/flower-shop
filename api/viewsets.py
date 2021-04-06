from rest_framework import viewsets

from api.serializers import ColorSerializer
from main.models import Color


class ColorViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'list')
    pagination_class = None
    queryset = Color.objects.active()
    serializer_class = ColorSerializer



