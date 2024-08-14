from django.urls import path
from .views import register, home, success, login_view
from django.contrib.auth import views as auth_views

# app_name = 'accounts'

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('success/', success, name='success'),
    path('login/', login_view, name='login'),
    path('password-reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
]
