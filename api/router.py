from rest_framework.routers import DefaultRouter

from api.viewsets import ColorViewSet, CategoryViewSet, ReasonViewSet, FlowerViewSet


router = DefaultRouter()
router.register(r'colors', ColorViewSet)
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'reasons', ReasonViewSet)
router.register(r'flowers', FlowerViewSet)
