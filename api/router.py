from rest_framework.routers import DefaultRouter

from api.viewsets import ColorViewSet


router = DefaultRouter()
router.register(r'colors', ColorViewSet, basename='colors')

