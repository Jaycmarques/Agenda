# accounts/tests/test_views.py
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from faker import Faker


@pytest.mark.django_db
def test_index_view(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert 'Welcome' in response.content.decode()


fake = Faker()


@pytest.mark.django_db
def test_register_view(client):
    # Generate a unique email
    email = fake.email()
    response = client.post(reverse('register'), data={
        'email': email,  # Use the generated unique email
        'first_name': fake.first_name(),
        'password1': 'newpassword',
        'password2': 'newpassword',
    })

    # Check if the response is a redirect (302) after successful registration
    # Expect a redirect status after successful registration
    assert response.status_code == 302

    # Verify that a user with the given email was created
    User = get_user_model()
    # Check if the user exists
    assert User.objects.filter(email=email).exists()
