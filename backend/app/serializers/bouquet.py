from rest_framework import serializers

from app.models import BaseBouquet, Product, BouquetFlower


class BouquetFlowerSerializer(serializers.ModelSerializer):
    flower_title = serializers.SerializerMethodField()

    def get_flower_title(self, obj):
        return obj.flower.title

    class Meta:
        model = BouquetFlower
        fields = ('count', 'flower_title',)


class BouquetSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(source='bouquet_price')
    flowers = BouquetFlowerSerializer(source='bouquetflower_set', many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            'price',
            'flowers',
        )


class BaseBouquetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseBouquet
        fields = (
            'id',
            'title',
            'is_new',
            'is_hit',
            'description',
            'photo_url',
            'min_price',
            'max_price',
        )


class BaseBouquetDetailSerializer(serializers.ModelSerializer):
    bouquets = serializers.SerializerMethodField()

    def get_bouquets(self, base):
        return BouquetSerializer(base.bouquets.all(), many=True).data

    class Meta:
        model = BaseBouquet
        fields = (
            'id',
            'title',
            'is_new',
            'is_hit',
            'color',
            'description',
            'photo_url',
            'min_price',
            'max_price',
            'bouquets',
        )
