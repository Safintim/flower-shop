from rest_framework import serializers

from app.models import BaseBouquet


class BouquetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseBouquet
        fields = (
            'id',
            'title',
            'description',
            'photo_url',
            'price',
        )
