from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Quote, Like, Comment


class QuoteTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.quote = Quote.objects.create(text='Test Quote', author='Test Author', category='General')

    def test_quote_creation(self):
        self.assertEqual(self.quote.text, 'Test Quote')
        self.assertEqual(self.quote.author, 'Test Author')
        self.assertEqual(self.quote.category, 'General')


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.search_url = reverse('search')
        self.category_url = reverse('category_view', args=['General'])

    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)

    def test_search_view(self):
        response = self.client.get(self.search_url)
        self.assertEqual(response.status_code, 200)

    def test_category_view(self):
        response = self.client.get(self.category_url)
        self.assertEqual(response.status_code, 200)


class SearchTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.search_url = reverse('search')
        Quote.objects.create(text='Test Quote', author='Test Author', category='General')

    def test_search_quote(self):
        response = self.client.get(self.search_url, {'query': 'Test Quote'})
        self.assertContains(response, 'Test Quote')
