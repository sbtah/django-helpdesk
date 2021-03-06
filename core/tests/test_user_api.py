from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('api:register-user')


# Helper function for faster user creation.
def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTest(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload successful."""

        payload = {
            'email': 'test@test.com',
            'full_name': 'Stefan',
            'password': 'testpass123',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email='test@test.com')
        # Checks if user created user have a password.
        self.assertTrue(user.check_password('testpass123'))
        # For security reasons password should not be in response.
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating a user that already exists in database."""
        payload = {
            'email': 'test@test.com',
            'full_name': 'Stefan',
            'password': 'testpass123',
        }
        # Helper funtion used.
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        # Checks for status code 400 if user already exists.
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 5 characters."""
        payload = {
            'email': 'test@test.com',
            'full_name': 'Stefan',
            'password': '123',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        # Checks that response is 400 cause password is too short.
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        # Checks that provided email for user already exists in db.
        user_exists = get_user_model().objects.filter(
            email=payload['email']).exists()
        self.assertFalse(user_exists)


# NEW TESTS!
