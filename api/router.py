from rest_framework.routers import DefaultRouter

from api.viewsets import ColorViewSet, CategoryViewSet, ReasonViewSet, FlowerViewSet, CallbackViewSet, ReviewViewSet


router = DefaultRouter()
router.register(r'colors', ColorViewSet)
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'reasons', ReasonViewSet)
router.register(r'flowers', FlowerViewSet)
router.register(r'callback', CallbackViewSet)
router.register(r'review', ReviewViewSet)
