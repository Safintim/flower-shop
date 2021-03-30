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

    path('', views.IndexTemplateView.as_view(), name='index'),
]
