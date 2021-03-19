from django.urls import path

from cart.views import CartProductListView, AddProductToCartView


urlpatterns = [
    path('', CartProductListView.as_view(), name='cart-product-update'),
    path('add/<int:product_pk>/', AddProductToCartView.as_view(), name='cart-product-create'),
]
