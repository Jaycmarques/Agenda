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
