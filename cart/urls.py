from django.urls import path

from cart import views


urlpatterns = [
    path('', views.CartProductListView.as_view(), name='cart-product-update'),
    path('add/<int:product_pk>/', views.AddProductToCartView.as_view(), name='cart-product-create'),
    path('delete/<int:pk>/', views.DeleteProductFromCartView.as_view(), name='cart-product-delete'),
]
