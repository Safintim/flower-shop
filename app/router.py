from rest_framework.routers import DefaultRouter

from app.viewsets.bouquet import BouquetViewSet

router = DefaultRouter()
router.register('bouquets', BouquetViewSet, basename='bouquets')
