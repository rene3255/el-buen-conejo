from django.urls import resolve
from django.test import TestCase
from homepage.views import homepage

class HomePageTest(TestCase):
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)
              