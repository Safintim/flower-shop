from django.urls import path

from custom_admin import views

urlpatterns = [
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),

    path('reasons/<int:pk>/delete/', views.ReasonDeleteView.as_view(), name='reason-delete'),
    path('reasons/create/', views.ReasonCreateView.as_view(), name='reason-create'),
    path('reasons/<int:pk>/', views.ReasonUpdateView.as_view(), name='reason-update'),
    path('reasons/', views.ReasonListView.as_view(), name='reason-list'),

    path('colors/<int:pk>/delete/', views.ColorDeleteView.as_view(), name='color-delete'),
    path('colors/create/', views.ColorCreateView.as_view(), name='color-create'),
    path('colors/<int:pk>/', views.ColorUpdateView.as_view(), name='color-update'),
    path('colors/', views.ColorListView.as_view(), name='color-list'),

    path('flowers/<int:pk>/delete/', views.FlowerDeleteView.as_view(), name='flower-delete'),
    path('flowers/create/', views.FlowerCreateView.as_view(), name='flower-create'),
    path('flowers/<int:pk>/', views.FlowerUpdateView.as_view(), name='flower-update'),
    path('flowers/', views.FlowerListView.as_view(), name='flower-list'),

    path('reviews/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review-delete'),
    path('reviews/create/', views.ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', views.ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/', views.ReviewListView.as_view(), name='review-list'),

    path('callbacks/<int:pk>/delete/', views.CallbackDeleteView.as_view(), name='callback-delete'),
    path('callbacks/create/', views.CallbackCreateView.as_view(), name='callback-create'),
    path('callbacks/<int:pk>/', views.CallbackUpdateView.as_view(), name='callback-update'),
    path('callbacks/', views.CallbackListView.as_view(), name='callback-list'),

    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),
    path('users/create/', views.UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', views.UserUpdateView.as_view(), name='user-update'),
    path('users/', views.UserListView.as_view(), name='user-list'),

    path('carts/', views.CartListView.as_view(), name='cart-list'),
    path('carts/<int:pk>/', views.CartDetailView.as_view(), name='cart-detail'),

    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-update'),


    path('configurations/', views.ConfigurationUpdateView.as_view(), name='configuration-update'),

    path('products/present/<int:pk>/', views.ProductPresentUpdateView.as_view(), name='product-present-update'),
    path('products/bouquet/<int:pk>/', views.ProductBouquetUpdateView.as_view(), name='product-bouquet-update'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/present/create/', views.ProductPresentCreateView.as_view(), name='product-present-create'),
    path('products/bouquet/create/', views.ProductBouquetCreateView.as_view(), name='product-bouquet-create'),

    path('products/<int:pk>/delete/', views.FlowerDeleteView.as_view(), name='product-delete'),

    path('', views.IndexTemplateView.as_view(), name='index'),
]
