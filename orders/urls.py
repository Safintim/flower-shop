from django.urls import path

from orders import views


urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('', views.OrderListView.as_view(), name='order-list'),
]
