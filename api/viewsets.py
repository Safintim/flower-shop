from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api.filters import ProductFilter
from api.serializers import (
    AddBouquetToCartSerializer,
    AddPresentToCartSerializer,
    BouquetsBySizeSerializer,
    CallbackSerializer,
    CartSerializer,
    ColorSerializer,
    CategorySerializer,
    DeleteProductFromCartSerializer,
    FlowerSerializer,
    ReasonSerializer,
    ReviewSerializer,
    OrderSerializer,
    OrderCreateSerializer,
    ProductSerializer, ProductPresentCreateSerializer, ProductBouquetCreateSerializer,
)
from cart.models import Cart, CartProduct
from core.models import Callback
from main.models import Color, Category, Reason, Flower, Product
from orders.models import Order
from reviews.models import Review


class BaseModelViewSet(ModelViewSet):
    http_method_names = ('get', 'list')
    pagination_class = None


class ColorViewSet(BaseModelViewSet):
    queryset = Color.objects.active()
    serializer_class = ColorSerializer


class CategoryViewSet(BaseModelViewSet):
    queryset = Category.objects.active().filter(parent=None)
    serializer_class = CategorySerializer


class ReasonViewSet(BaseModelViewSet):
    queryset = Reason.objects.active()
    serializer_class = ReasonSerializer


class FlowerViewSet(BaseModelViewSet):
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


class BaseGenericViewSet(GenericViewSet):
    serializer_classes_by_action = {}
    permission_classes_by_action = {}

    def get_serializer_class(self):
        try:
            return self.serializer_classes_by_action[self.action]
        except (AttributeError, KeyError):
            return super().get_serializer_class()

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except (AttributeError, KeyError):
            return super().get_permissions()

    def validate_serializer(self, request, **kwargs):
        context = self.get_serializer_context()
        context.update(kwargs)
        serializer = self.get_serializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        return serializer


class CartViewSet(BaseGenericViewSet):
    http_method_names = ('get', 'post', 'delete')
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    serializer_classes_by_action = {
        'list': CartSerializer,
        'add_present': AddPresentToCartSerializer,
        'add_bouquet': AddBouquetToCartSerializer,
        'delete_product': DeleteProductFromCartSerializer
    }

    def list(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

    def validate_serializer(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer

    def response_after_add(self, cart):
        cart_serializer = self.serializer_class(cart, context={'request': self.request}).data
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


class OrderViewSet(BaseGenericViewSet):
    http_method_names = ('get', 'post')
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    serializer_classes_by_action = {
        'list': serializer_class,
        'create': OrderCreateSerializer
    }

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def is_exists_cart_product(self, request):
        return CartProduct.objects.filter(cart__user=request.user).exists()

    def create(self, request):
        if not self.is_exists_cart_product(request):
            return Response({'detail': 'cart products does not exist'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.validate_serializer(request)
        order = serializer.save(user=request.user)
        order.create_order_products()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductViewSet(ListModelMixin, BaseGenericViewSet):
    http_method_names = ('get', 'post')
    queryset = Product.objects.active()
    filterset_class = ProductFilter
    serializer_class = ProductSerializer
    serializer_classes_by_action = {
        'list': serializer_class,
        'create_present': ProductPresentCreateSerializer,
        'create_bouquet': ProductBouquetCreateSerializer,
        'bouquets': BouquetsBySizeSerializer
    }
    permission_classes_by_action = {
        'create_present': (permissions.IsAdminUser,),
        'create_bouquet': (permissions.IsAdminUser,),
        'bouquets': (permissions.IsAdminUser,),
    }

    def get_queryset(self):
        if self.action == 'add_bouquets':
            return Product.objects.all()
        return super().get_queryset()

    @action(detail=False, methods=['post'], url_name='create-present')
    def create_present(self, request):
        serializer = self.validate_serializer(request)
        serializer.save(type=Product.Type.PRESENT)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_name='create-bouquet')
    def create_bouquet(self, request):
        serializer = self.validate_serializer(request)
        serializer.save(type=Product.Type.BOUQUET)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def bouquets(self, request, **kwargs):
        product = self.get_object()
        serializer = self.validate_serializer(request, product=product)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
