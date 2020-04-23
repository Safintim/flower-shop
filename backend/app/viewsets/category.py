from rest_framework import viewsets

from app.models import Category
from app.serializers.category import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    http_method_names = ['options', 'get']
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(parent=None)
