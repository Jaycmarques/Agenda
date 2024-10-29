import pytest
from django.test import TestCase
from django.urls import reverse, resolve
from accounts import views
from django.contrib.auth import get_user_model
from faker import Faker
from accounts.models import Category, Account, User


class AccountsViewsTest(TestCase):
    def test_home_view_function_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, views.home)

    def test_search_view_function_is_correct(self):
        view = resolve(reverse('search'))
        self.assertIs(view.func, views.search)

    def test_contact_view_function_is_correct(self):
        view = resolve(
            reverse('contact', kwargs={'contact_id': 1}))
        self.assertIs(view.func, views.contact)


@pytest.mark.django_db
def test_index_view_statuscode_ok(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert 'Welcome' in response.content.decode()


def test_index_view_loads_correct_template_ok(client):
    response = client.get(reverse('index'))
    assert 'accounts/index.html' in [t.name for t in response.templates]


fake = Faker()


@pytest.mark.django_db
def test_register_is_ok(client):
    # Generate a unique email
    email = fake.email()
    response = client.post(reverse('register'), data={
        'email': email,  # Use the generated unique email
        'first_name': fake.first_name(),
        'password1': 'newpassword123!',
        'password2': 'newpassword123!',
    })

    assert response.status_code == 302

    # Verify that a user with the given email was created
    User = get_user_model()
    # Check if the user exists
    assert User.objects.filter(email=email).exists()
