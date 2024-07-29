import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_user_registration(client):
    response = client.post(reverse('register'), {
        'username': 'testuser',
        'password1': 'securepassword123',
        'password2': 'securepassword123'
    })
    # Espera-se redirecionamento após registro bem-sucedido
    assert response.status_code == 302
    # Verifique a URL de redirecionamento
    assert response.url == reverse('home')
