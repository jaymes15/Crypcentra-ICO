from core import models
from datetime import timedelta
from django.utils import timezone


def current_date():
    """Create current date object"""
    return timezone.now()


def create_coin(user):
    """Creates coin model object"""
    return models.Coin.objects.create(
        name="My coin",
        owner=user,
        description="Best coin",
        bidding_window=current_date() + timedelta(days=10)
    )
