from django.urls import path

from main import views


urlpatterns = [
    path('catalog/product/<str:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('catalog/all/', views.BouquetListView.as_view(), name='product-list'),
    path('catalog/filter/', views.ProductFilterView.as_view(), name='product-list-filter'),
    path('catalog/<str:slug>/', views.ProductByCategoryListView.as_view(), name='product-by-category'),
    path('', views.IndexTemplateView.as_view(), name='index'),
]
