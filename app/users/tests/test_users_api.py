from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


TOKEN_URL = reverse("users:token")
CREATE_USER_URL = reverse("users:create")


def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating using with a valid payload is successful"""
        payload = {
            "username": "JohnDoe",
            "email": "test@domain.com",
            "password": "testpass",
        }

        res = self.client.post(CREATE_USER_URL, payload)
        user = get_user_model().objects.get(username=payload["username"])

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_user_exists(self):
        """Test creating a user that already exists fails"""
        payload = {
            "username": "JohnDoe",
            "email": "test@domain.com",
            "password": "testpass",
        }

        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {
            "username": "JohnDoe",
            "email": "test@domain.com",
            "password": "testpass",
        }

        create_user(**payload)

        res = self.client.post(TOKEN_URL, payload)

        self.assertIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_no_user(self):
        """Test that token is not created if user doens't exist"""
        payload = {"username": "JohnDoe", "password": "testpass"}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        res = self.client.post(TOKEN_URL,
                               {"username": "JohnDoe",
                                "password": ""})

        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
