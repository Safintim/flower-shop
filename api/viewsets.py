from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import (
    CallbackSerializer,
    CartSerializer,
    ColorSerializer,
    CategorySerializer,
    FlowerSerializer,
    ReasonSerializer,
    ReviewSerializer,
)
from cart.models import Cart
from core.models import Callback
from main.models import Color, Category, Reason, Flower
from reviews.models import Review


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


class DisableRetrieveMixin:
    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)


class ReviewViewSet(DisableRetrieveMixin, ModelViewSet):
    http_method_names = ('get', 'post')
    queryset = Review.objects.active()
    serializer_class = ReviewSerializer


class CartViewSet(DisableRetrieveMixin, ModelViewSet):
    http_method_names = ('get', 'post')
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def list(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)
