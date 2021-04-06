from rest_framework.serializers import ModelSerializer

from cart.models import Cart, CartProduct
from core.models import Callback
from main.models import Color, Category, Reason, Flower, Product, Bouquet, BouquetFlower
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


class ProductSerializer(ModelSerializer):
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
