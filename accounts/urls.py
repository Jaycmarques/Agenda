from django.urls import path
from .views import register, home, success, log_in
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('success/', success, name='success'),
    path('login/', log_in, name='login'),
    path('password-reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
]
