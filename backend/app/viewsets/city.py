from rest_framework import viewsets

from app.models import City
from app.serializers.city import CitySerializer


class CityViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'options']
    queryset = City.objects.all()
    serializer_class = CitySerializer
