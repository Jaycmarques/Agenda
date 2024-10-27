from django.test import TestCase
from django.urls import reverse, resolve
from accounts import views


class AccountsViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('accounts:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_search_view_function_is_correct(self):
        view = resolve(reverse('accounts:search'))
        self.assertIs(view.func, views.search)

    def test_recipe_contact_view_function_is_correct(self):
        view = resolve(
            reverse('accounts:contact', kwargs={'contact_id': 1}))
        self.assertIs(view.func, views.contact)
