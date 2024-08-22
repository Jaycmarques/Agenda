# accounts/views.py
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout

from accounts.contact_forms import AccountForm
from .forms import CustomUserCreationForm
from accounts.models import Account
from django.db.models import Q
from django.core.paginator import Paginator


def index(request):
    return render(request, 'accounts/index.html')


def home(request):
    accounts = Account.objects.filter(show=True)
    paginator = Paginator(accounts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    print(accounts.query)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'accounts/home.html', context)


def search(request):

    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('home')

    accounts = Account.objects.filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(email__icontains=search_value)

    )\

    paginator = Paginator(accounts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    print(accounts.query)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'accounts/home.html', context)


def contact(request, contact_id):
    single_contact = get_object_or_404(Account, pk=contact_id, show=True)
    context = {
        'contact': single_contact,
    }
    return render(request, 'accounts/contact.html', context)


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


def logout_view(request):
    logout(request)
    return redirect('login')


def password_reset(request):
    return render(request, 'accounts/password_reset.html')


def create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            # Se o formulário for válido, você pode salvar o objeto ou fazer outra coisa.
            form.save()
            # Redirecione para uma URL de sucesso ou página relevante
            return redirect('success')
    else:
        form = AccountForm()

    return render(request, 'accounts/create.html', {'form': form})
