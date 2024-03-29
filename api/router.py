from rest_framework.routers import DefaultRouter

from api.viewsets import (
    CategoryViewSet,
    CallbackViewSet,
    CartViewSet,
    ColorViewSet,
    FlowerViewSet,
    OrderViewSet,
    ReasonViewSet,
    ReviewViewSet,
    ProductViewSet,
)


router = DefaultRouter()
router.register(r'colors', ColorViewSet)
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'reasons', ReasonViewSet)
router.register(r'flowers', FlowerViewSet)
router.register(r'callback', CallbackViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'cart', CartViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'products', ProductViewSet)
