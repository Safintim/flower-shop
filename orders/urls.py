from django.urls import path

from orders import views


urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('check/<int:pk>/', views.OrderCheckStatusShow.as_view(), name='order-check-status-show'),
    path('check/', views.OrderCheckStatus.as_view(), name='order-check-status'),
]
