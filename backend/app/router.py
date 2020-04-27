from rest_framework.routers import DefaultRouter

from app import viewsets

router = DefaultRouter()
router.register('bouquets', viewsets.BouquetViewSet, basename='bouquets')
router.register('categories', viewsets.CategoryViewSet, basename='categories')
router.register('cities', viewsets.CityViewSet, basename='cities')
