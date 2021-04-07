from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api.serializers import (
    AddBouquetToCartSerializer,
    AddPresentToCartSerializer,
    CallbackSerializer,
    CartSerializer,
    ColorSerializer,
    CategorySerializer,
    DeleteProductFromCartSerializer,
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


class CartViewSet(GenericViewSet):
    http_method_names = ('get', 'post', 'delete')
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    serializer_action_classes = {
        'list': CartSerializer,
        'add_present': AddPresentToCartSerializer,
        'add_bouquet': AddBouquetToCartSerializer,
        'delete_product': DeleteProductFromCartSerializer
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (AttributeError, KeyError):
            return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

    def validate_serializer(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer

    def response_after_add(self, cart):
        cart_serializer = self.serializer_class(cart).data
        return Response(cart_serializer, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_name='add-present')
    def add_present(self, request):
        serializer = self.validate_serializer(request)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart.add_product(serializer.instance)
        return self.response_after_add(cart)

    @action(detail=False, methods=['post'], url_name='add-bouquet')
    def add_bouquet(self, request):
        serializer = self.validate_serializer(request)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart.add_product(serializer.instance, bouquet_size=serializer.validated_data['bouquet_size'])
        return self.response_after_add(cart)

    @action(detail=False, methods=['delete'], url_name='delete-product')
    def delete_product(self, request):
        serializer = self.validate_serializer(request)
        serializer.instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
