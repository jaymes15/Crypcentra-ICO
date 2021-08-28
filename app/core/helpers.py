
from django.contrib.auth import get_user_model


def sample_user(
        username="JohnDoe",
        email="johndoe@mail.com",
        password="testpassword",
        first_name="John",
        last_name="Doe"):
    """Helper to create sample user"""
    return get_user_model().objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
