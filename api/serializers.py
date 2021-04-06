from rest_framework.serializers import ModelSerializer

from core.models import Callback
from main.models import Color, Category, Reason, Flower
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
        fields = ('phone', 'name', 'city', 'image', 'social_link', 'text')
