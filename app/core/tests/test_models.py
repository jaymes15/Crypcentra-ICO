from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from core import models
from core.tests import utils
from core.helpers import sample_user
from datetime import timedelta


class TestCoinModel(TestCase):

    def setUp(self):
        self.user = sample_user()

    def test_create_coin(self):
        """Test coin can be created"""

        coin = utils.create_coin(self.user)
        coin_query = models.Coin.objects.last()

        self.assertEquals(coin_query, coin)

    def test_coin_name_is_unique(self):
        """Test coin name is unique"""

        utils.create_coin(self.user)

        with self.assertRaises(IntegrityError):
            utils.create_coin(self.user)

    def test_date_validator(self):
        """Test Coin object with past date can not be created"""
        current_date = utils.current_date()
        coin = models.Coin(
            name="My coin",
            owner=self.user,
            description="Best coin",
            bidding_window=current_date - timedelta(days=10),
            number_of_available_token=123.5,
        )

        self.assertRaises(ValidationError, coin.full_clean)

    def test_str_return(self):
        """Test CoinModel str method"""

        coin = utils.create_coin(self.user)
        coin_query = models.Coin.objects.last()

        self.assertEquals(str(coin_query), str(coin))


class TestBidModel(TestCase):

    def setUp(self):
        self.user = sample_user()

    def test_create_bid(self):
        """Test bid can be created"""

        bid = utils.create_bid(self.user)
        bid_query = models.Bid.objects.last()

        self.assertEquals(bid_query, bid)

    def test_user_can_bid_for_different_coins(self):
        """Test user can bid for different coin"""

        first_coin_bid = utils.create_bid(self.user)
        second_coin_bid = utils.create_bid(self.user,
                                           "my other coin")

        self.assertIsNotNone(first_coin_bid)
        self.assertIsNotNone(second_coin_bid)

    def test_str_return(self):
        """Test BidModel str method"""

        bid = utils.create_bid(self.user)
        bid_query = models.Bid.objects.last()

        self.assertEquals(str(bid_query), str(bid))
