# accounts/views.py
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'accounts/home.html')


@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def success(request):
    return render(request, 'accounts/success.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página home
    return render(request, 'accounts/login.html')


def password_reset(request):
    return render(request, 'accounts/password_reset.html')
