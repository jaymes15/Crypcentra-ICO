from django.db import models
from django.contrib.auth.models import User


class Coin(models.Model):
    """Coin Model"""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE)
    number_of_available_token = models.DecimalField(max_digits=10,
                                                    decimal_places=5)
    created_on = models.DateTimeField(auto_now=True)
    bidding_window = models.DateTimeField()

    def __str__(self):
        return f'{self.owner}: {self.name}'
