from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from core.model_validators.validate_date import validate_date
from core.utils import current_date


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
        if self.bidding_window.date() <= current_date().date():
            raise ValidationError("bidding window has to be a future date")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Bid(models.Model):
    """Bid Model"""
    STATUS = (
        ('recieved some', 'RECIEVED SOME'),
        ('recieved all', 'RECIEVED ALL'),
        ('none', 'None')
    )

    coin = models.ForeignKey(
        Coin, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    number_of_tokens = models.DecimalField(max_digits=10,
                                           decimal_places=5)
    bidding_price = models.PositiveIntegerField()
    token_recieved = models.DecimalField(max_digits=10,
                                         decimal_places=5,
                                         blank=True,
                                         null=True)
    status = models.CharField(max_length=30,
                              choices=STATUS,
                              default="None")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}: {self.coin}'
