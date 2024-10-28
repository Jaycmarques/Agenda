from django.test import TestCase
from django.urls import reverse


class AccountsURLsTest(TestCase):
    def test_url_index_ok(self):
        url = reverse('index')
        self.assertEqual(url, '/')

    def test_url_home_ok(self):
        url = reverse('home')
        self.assertEqual(url, '/home/')

    def test_url_contact_detail_ok(self):
        url = reverse('contact', args=(1,))
        self.assertEqual(url, '/contact/1/detail/')

    def test_url_search_ok(self):
        url = reverse('search')
        self.assertEqual(url, '/search/')

    def test_url_register_ok(self):
        url = reverse('register')
        self.assertEqual(url, '/register/')

    def test_url_success_ok(self):
        url = reverse('success')
        self.assertEqual(url, '/success/')

    def test_url_login_ok(self):
        url = reverse('login')
        self.assertEqual(url, '/login/')

    def test_url_logout_ok(self):
        url = reverse('logout')
        self.assertEqual(url, '/logout/')
