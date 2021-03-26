from django.urls import path

from core import views


urlpatterns = [
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('shipping/', views.ShippingAndPaymentTemplateView.as_view(), name='shipping'),
    path('contacts/', views.ContactsTemplateView.as_view(), name='contacts'),
    path('callback/create/', views.CallbackView.as_view(), name='callback-create'),
]
