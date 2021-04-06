from rest_framework.viewsets import ModelViewSet

from api.serializers import ColorSerializer, CategorySerializer, ReasonSerializer, FlowerSerializer, CallbackSerializer
from core.models import Callback
from main.models import Color, Category, Reason, Flower


class BaseViewSet(ModelViewSet):
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
    queryset = Flower.objects.active().is_add_filter()
    serializer_class = FlowerSerializer


class CallbackViewSet(ModelViewSet):
    http_method_names = ('post',)
    queryset = Callback.objects.all()
    serializer_class = CallbackSerializer
