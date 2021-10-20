from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Coin
from core.tests import utils
from coins.serializers import CoinListSerializer, CoinSerializer
from core.helpers import sample_user
from datetime import timedelta

COINS_URL = reverse("coins:coins-list")


def get_coins_detail_url(id):

    return reverse("coins:coins-detail", args=[id])


class TestCoinView(TestCase):
    def setUp(self):
        self.user = sample_user()
        self.another_user = sample_user("another_user")
        self.client = APIClient()

    def test_create_coins(self):
        """Test CREATE coins"""
        self.client.force_authenticate(user=self.user)

        current_date = utils.current_date()
        payload = {
            "name": "jaycoins",
            "description": "my coins",
            "bidding_window": current_date + timedelta(days=10),
            "number_of_available_token": 123.5,
        }
        response = self.client.post(COINS_URL, data=payload)
        coin_query = Coin.objects.last()
        serializer = CoinSerializer(coin_query, many=False)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data == serializer.data

    def test_get_coins(self):
        """Test GET"""

        utils.create_coin(self.user)

        response = self.client.get(COINS_URL)
        all_coins = Coin.objects.all()
        serializer = CoinListSerializer(all_coins, many=True)

        assert response.status_code == status.HTTP_200_OK
        assert response.data is not None
        assert serializer.data == response.data

    def test_get_coins_created_by_user(self):
        """Test get coins created by user"""
        self.client.force_authenticate(user=self.user)
        utils.create_coin(self.user)

        response = self.client.get(COINS_URL)
        user_coins = Coin.objects.filter(owner=self.user.id)
        serializer = CoinListSerializer(user_coins, many=True)

        assert response.status_code == status.HTTP_200_OK
        assert response.data is not None
        assert serializer.data == response.data

    def test_get_coin_by_query_params(self):
        """Test get coin by query params"""

        self.client.force_authenticate(user=self.user)

        coin = utils.create_coin(self.user)
        response = self.client.get(COINS_URL, {"coin_name": coin.name})
        coin_query = Coin.objects.filter(name=coin.name)
        serializer = CoinListSerializer(coin_query, many=True)

        assert response.status_code == status.HTTP_200_OK
        assert serializer.data == response.data
