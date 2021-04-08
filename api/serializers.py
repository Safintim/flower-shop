from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer, HyperlinkedModelSerializer

from cart.models import Cart, CartProduct
from core.models import Callback
from main.models import Color, Category, Reason, Flower, Product, Bouquet, BouquetFlower
from orders.models import Order, OrderProduct
from reviews.models import Review


class BaseSerializer:
    fields = ('id', 'title')


class ColorSerializer(ModelSerializer):
    class Meta(BaseSerializer):
        model = Color


class CategoryChildrenSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = BaseSerializer.fields + ('slug',)


class CategorySerializer(ModelSerializer):
    children = CategoryChildrenSerializer(many=True)

    class Meta:
        model = Category
        fields = BaseSerializer.fields + ('slug', 'children')


class ReasonSerializer(ModelSerializer):
    class Meta(BaseSerializer):
        model = Reason


class FlowerSerializer(ModelSerializer):
    class Meta:
        model = Flower
        fields = BaseSerializer.fields


class CallbackSerializer(ModelSerializer):
    class Meta:
        model = Callback
        fields = ('phone',)


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'phone', 'name', 'city', 'image', 'social_link', 'text')


class ProductSerializer(HyperlinkedModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='product-detail', read_only=True, lookup_field='slug')

    class Meta:
        model = Product
        fields = (
            'id',
            'type',
            'slug',
            'price',
            'discount',
            'is_hit',
            'is_new',
            'small_image',
            'detail'
        )


class BouquetFlowerSerializer(ModelSerializer):
    class Meta:
        model = BouquetFlower
        fields = ('count', 'flower')


class BouquetSerializer(ModelSerializer):
    flowers = BouquetFlowerSerializer(source='flowers_set', many=True, read_only=True)

    class Meta:
        model = Bouquet
        fields = ('id', 'size', 'price', 'flowers')


class CartProductSerializer(ModelSerializer):
    bouquet = BouquetSerializer()
    product = ProductSerializer()

    class Meta:
        model = CartProduct
        fields = ('product', 'bouquet', 'qty', 'price')


class CartSerializer(ModelSerializer):
    products = CartProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('product_total', 'price_total', 'products')


class AddPresentToCartSerializer(Serializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        qs = Product.objects.active().filter(pk=value)
        self.instance = qs.first()
        if not qs.exists():
            raise serializers.ValidationError('product does not exist')
        return value


class AddBouquetToCartSerializer(AddPresentToCartSerializer):
    bouquet_size = serializers.ChoiceField(choices=Bouquet.Size)

    def validate_bouquet_size(self, value):
        product = self.instance
        if not (product and product.get_bouquet_by_size(size=value)):
            raise serializers.ValidationError('bouquet does not exist')
        return value


class DeleteProductFromCartSerializer(Serializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        user = self.context['request'].user

        qs = CartProduct.objects.filter(cart__user=user, product_id=value)
        self.instance = qs.first()
        if not qs.exists():
            raise serializers.ValidationError('cart product does not exist')
        return value


class OrderProductSerializer(ModelSerializer):
    bouquet = BouquetSerializer()
    product = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = ('product', 'bouquet', 'price', 'qty')


class OrderSerializer(ModelSerializer):
    code = serializers.IntegerField(source='pk')
    products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('code', 'created_at', 'delivery_date', 'delivery_time', 'status', 'price_total', 'products')


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'recipient',
            'recipient_name',
            'recipient_phone',
            'recipient_address',
            'recipient_call',
            'delivery_type',
            'delivery_date',
            'delivery_time',
            'postcard',
            'postcard_text',
            'comment',
        )
