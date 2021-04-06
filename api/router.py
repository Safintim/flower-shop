from rest_framework.routers import DefaultRouter

from api.viewsets import ColorViewSet, CategoryViewSet


router = DefaultRouter()
router.register(r'colors', ColorViewSet)
router.register(r'categories', CategoryViewSet, basename='category')

