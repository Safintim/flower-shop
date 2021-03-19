from django.urls import path

from cart.views import CartProductListView


urlpatterns = [
    path('', CartProductListView.as_view(), name='cart-product-update'),
]
