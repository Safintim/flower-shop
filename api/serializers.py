from rest_framework.serializers import ModelSerializer

from main.models import Color, Category


class ConfigSerializer:
    common_fields = ('id', 'title')


class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = ConfigSerializer.common_fields


class CategoryChildrenSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ConfigSerializer.common_fields + ('slug',)


class CategorySerializer(ModelSerializer):
    children = CategoryChildrenSerializer(many=True)

    class Meta:
        model = Category
        fields = ConfigSerializer.common_fields + ('slug', 'children')
