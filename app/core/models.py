from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from core.model_validators.validate_date import validate_date
from core import utils


class Coin(models.Model):
    """Coin Model"""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE)
    number_of_available_token = models.DecimalField(max_digits=10,
                                                    decimal_places=5)
    created_on = models.DateTimeField(auto_now=True)
    bidding_window = models.DateTimeField(validators=[validate_date])

    def __str__(self):
        return f'{self.owner}: {self.name}'

    def clean(self):
        if self.bidding_window <= utils.current_date():
            raise ValidationError("bidding window has to be a future date")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Bid(models.Model):
    """Bid Model"""
    coin = models.ForeignKey(
        Coin, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    number_of_tokens = models.DecimalField(max_digits=10,
                                           decimal_places=5)
    bidding_price = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}: {self.coin}'

    def is_bidding_window_open(self):
        """Check if coin bidding window is open"""
        if self.coin.bidding_window <= utils.current_date():
            raise ValidationError("bidding window is closed")

    def clean(self):
        self.is_bidding_window_open()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
