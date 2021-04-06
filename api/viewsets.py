from rest_framework import viewsets

from api.serializers import ColorSerializer, CategorySerializer, ReasonSerializer, FlowerSerializer
from main.models import Color, Category, Reason, Flower


class BaseViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'list')
    pagination_class = None


class ColorViewSet(BaseViewSet):
    queryset = Color.objects.active()
    serializer_class = ColorSerializer


class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.active().filter(parent=None)
    serializer_class = CategorySerializer


class ReasonViewSet(BaseViewSet):
    queryset = Reason.objects.active()
    serializer_class = ReasonSerializer


class FlowerViewSet(BaseViewSet):
    queryset = Flower.objects.active()
    serializer_class = FlowerSerializer
