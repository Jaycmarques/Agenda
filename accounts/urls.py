from django.urls import path
from .views import register, home, success, login_view, index, contact, logout_view
from django.contrib.auth import views as auth_views

# app_name = 'accounts'

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('<int:contact_id>/', contact, name='contact'),
    path('register/', register, name='register'),
    path('success/', success, name='success'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
]
