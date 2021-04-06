from rest_framework.serializers import ModelSerializer

from main.models import Color


class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'title')
