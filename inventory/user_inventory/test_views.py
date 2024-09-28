from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Items  # Adjust according to your app name
from .serializers import ItemSerializer  # Adjust according to your app name


class APITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')  # Log the user in
        self.item_url = reverse('add-item')  # Adjust according to your URL configuration
        self.item_detail_url = lambda item_id: reverse('item-detail', args=[item_id])  # Adjust accordingly

    def test_user_signup_success(self):
        url = reverse('user-signup')  # Adjust according to your URL configuration
        data = {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_signup_error(self):
        url = reverse('user-login')  # Adjust accordingly
        data = {
            'username': '',
            'password': 'test2',
            'email': 'test2@gmail.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_item_success(self):
        data = {
            'name': 'Test Item',
            'description': 'A test item description',
            'quantity': 10,
            'price': '99.99'
        }
        response = self.client.post(self.item_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Add more tests as previously discussed
