import pytest
from django.urls import reverse
from project.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('home'))
    return resp


def test_home_page_status_code(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200


def test_login_link(resp):
    login_url = reverse('login')
    assert_contains(resp, f'href="{login_url}"')


def test_register_link(resp):
    signup_url = reverse('register')
    assert_contains(resp, f'href="{signup_url}"')
