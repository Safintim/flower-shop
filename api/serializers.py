from rest_framework.serializers import ModelSerializer

from main.models import Color, Category, Reason, Flower


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
