from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserModelTest(TestCase):
    """Test case for custom user model and model manager."""

    def test_create_user_with_email_successful(self):
        """Test creating new user with email."""
        email = 'zorin@zorin.com'
        password = 'test123!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        email = 'zorin@ZORIN.com'
        password = 'test123!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123!')

    def test_create_new_superuser(self):
        """Test creating new super user."""
        user = get_user_model().objects.create_superuser(
            'zorin@zorin.com',
            'test123!',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)