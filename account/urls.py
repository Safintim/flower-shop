from django.urls import path

from account import views


urlpatterns = [
    path('my/', views.UserView.as_view(), name='user-detail'),
    path('my/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('registration/', views.UserRegistrationView.as_view(), name='user-registration')
]
