import copy
from PIL import Image
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


class BouquetFlowerSerializer(ModelSerializer):
    id = serializers.IntegerField(source='pk', required=False)

    class Meta:
        model = BouquetFlower
        fields = ('id', 'count', 'flower')


class BouquetSerializer(ModelSerializer):
    flowers = BouquetFlowerSerializer(source='flowers_set', many=True, read_only=True)

    class Meta:
        model = Bouquet
        fields = ('id', 'size', 'price', 'flowers')


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


class ProductValidateImageMixin:
    SMALL_RESOLUTION = (372, 372)
    BIG_RESOLUTION = (640, 640)

    def validate_image(self, image, sizes):
        image_obj = Image.open(image)
        width, height = sizes
        if image_obj.width != width or image_obj.height != height:
            raise serializers.ValidationError(f'Размер должен быть {width}x{height}', code='required')
        return image

    def validate_small_image(self, image):
        return self.validate_image(image, self.SMALL_RESOLUTION)

    def validate_big_image(self, image):
        return self.validate_image(image, self.BIG_RESOLUTION)


class ProductPresentCreateSerializer(ProductValidateImageMixin, ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'discount',
            'is_active',
            'is_hit',
            'is_new',
            'small_image',
            'big_image',
            'categories',
            'reasons',
        )

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.categories.add(Category.objects.filter(title='Подарки').first())
        return obj


class ProductBouquetCreateSerializer(ProductValidateImageMixin, ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'discount',
            'is_active',
            'is_hit',
            'is_new',
            'small_image',
            'big_image',
            'categories',
            'reasons',
            'color',
        )

    def create(self, validated_data):
        product = super().create(validated_data)
        if not product.get_middle_bouquet():
            product.is_active = False
            product.save()
        return product


class AddBouquetsSerializer(Serializer):
    SMALL = BouquetFlowerSerializer(many=True)
    MIDDLE = BouquetFlowerSerializer(many=True)
    BIG = BouquetFlowerSerializer(many=True)

    def create_bouquet_flowers(self, bouquet, flowers):
        qs = BouquetFlower.objects.filter(bouquet=bouquet)
        all_pks = list(qs.values_list('pk', flat=True))
        BouquetFlower.objects.bulk_create(
            [BouquetFlower(bouquet=bouquet, **flower) for flower in flowers]
        )
        return qs.exclude(pk__in=all_pks).values_list('pk', flat=True)

    def update_bouquet_flowers(self, bouquet, flowers):
        qs = BouquetFlower.objects.filter(bouquet=bouquet)
        flowers = copy.deepcopy(flowers)
        for flower in flowers:
            pk = flower.pop('pk')
            qs.filter(pk=pk).update(**flower)

    def delete_bouquet_flowers(self, bouquet, exclude_ids):
        BouquetFlower.objects.filter(bouquet=bouquet).exclude(id__in=exclude_ids).delete()

    def create_bouquet(self, product, size, flowers):
        bouquet = Bouquet.objects.create(size=size)
        self.create_bouquet_flowers(bouquet, flowers)
        product.bouquets.add(bouquet)

    def change_bouquet(self, bouquet, flowers):
        created_ids = self.create_bouquet_flowers(
            bouquet, filter(lambda flower: 'pk' not in flower, flowers)
        )
        self.update_bouquet_flowers(bouquet, filter(lambda flower: 'pk' in flower, flowers))
        updated_ids = list(map(lambda f: f['pk'], filter(lambda flower: 'pk' in flower, flowers)))
        exclude_flower_ids = list(created_ids) + updated_ids
        self.delete_bouquet_flowers(bouquet, exclude_flower_ids)

    def delete_bouquet(self, bouquet):
        bouquet.bouquetflower_set.all().delete()
        bouquet.delete()

    def create(self, validated_data):
        product = self.context.get('product')
        for size, flowers in validated_data.items():
            bouquet = product.get_bouquet_by_size(size)
            if not bouquet and flowers:
                self.create_bouquet(product, size, flowers)
            elif bouquet and not flowers:
                self.delete_bouquet(bouquet)
            elif bouquet and flowers:
                self.change_bouquet(bouquet, flowers)

        return product

    def to_representation(self, instance):
        return ProductSerializer(instance, context=self.context).data


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
