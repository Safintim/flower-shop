from django.urls import path

from custom_admin import views


urlpatterns = [
    path('categories/<int:pk>', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('', views.IndexTemplateView.as_view(), name='index'),
]
