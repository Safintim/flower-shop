from rest_framework import serializers

from app.models import Category


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        qs = Category.objects.filter(parent=obj)
        return CategorySerializer(qs, many=True).data

    class Meta:
        model = Category
        fields = (
            'title',
            'children',
        )
