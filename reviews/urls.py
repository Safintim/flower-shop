from django.urls import path

from reviews import views


urlpatterns = [
    path('', views.ReviewListView.as_view(), name='review-list'),
]
