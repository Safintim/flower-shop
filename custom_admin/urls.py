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

    path('products/<int:pk>/delete/', views.FlowerDeleteView.as_view(), name='product-delete'),
    path('products/present/create/', views.ProductPresentCreateView.as_view(), name='product-present-create'),
    path('products/bouquet/create/', views.ProductBouquetCreateView.as_view(), name='product-bouquet-create'),
    path('products/present/<int:pk>/', views.ProductPresentUpdateView.as_view(), name='product-present-update'),
    path('products/bouquet/<int:pk>/', views.ProductBouquetUpdateView.as_view(), name='product-bouquet-update'),
    path('products/bouquet/<int:pk>/small/create/', views.BouquetSmallCreateView.as_view(), name='bouquet-small-create'),
    path('products/', views.ProductListView.as_view(), name='product-list'),

    path('', views.IndexTemplateView.as_view(), name='index'),
]
