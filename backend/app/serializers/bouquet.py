from rest_framework import serializers

from app.models import BaseBouquet, Product


class BouquetSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(source='bouquet_price')

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            'price',
        )


class BaseBouquetSerializer(serializers.ModelSerializer):
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
            'description',
            'photo_url',
            'min_price',
            'max_price',
            'bouquets',
        )
