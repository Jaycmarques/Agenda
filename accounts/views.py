# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def success(request):
    return render(request, 'accounts/success.html')


def log_in(request):
    return render(request, 'accounts/login.html')


def password_reset(request):
    return render(request, 'accounts/password_reset.html')
