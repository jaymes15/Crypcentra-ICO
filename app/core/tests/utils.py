from datetime import timedelta

from django.utils import timezone

from core import models


def get_current_date():
    """Return current date object"""
    return timezone.now()


def sample_coin(user, name="My coin", token=123.5):
    """Creates coin model object"""
    return models.Coin.objects.create(
        name=name,
        owner=user,
        description="Best coin",
        bidding_window=get_current_date() + timedelta(days=10),
        number_of_available_token=token,
    )


def create_bid(user, name="My coin"):
    """Creates bid model object"""
    return models.Bid.objects.create(
        coin=sample_coin(user, name),
        user=user,
        number_of_tokens=12.5,
        bidding_price=1000,
    )
