from django.shortcuts import render
from django.urls import path

from main import views


def index(request):
    return render(request, 'base.html')


urlpatterns = [
    path('catalog/product/<str:slug>/', views.ProductDetail.as_view(), name='product-detail'),
    path('catalog/all/', views.ProductList.as_view(), name='product-list'),
    path('', index, name='index'),
]
