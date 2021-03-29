from django.urls import path

from custom_admin import views


urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='custom-admin-index'),
]
