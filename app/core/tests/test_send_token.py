from django.test import TestCase
from core.helpers import sample_user
from core.integrations.send_tokens import send_tokens
from core.tests import utils
from core import models
from datetime import timedelta
from unittest.mock import patch


class TestSendToken(TestCase):

    def setUp(self):
        self.main_user = sample_user("main_user")
        self.number_of_token = 28.0
        self.coin = utils.create_coin(
            self.main_user,
            token=self.number_of_token)

        self.create_users()
        self.create_bids()

    def create_users(self):
        """Create users"""
        self.user_1 = sample_user("user_1")
        self.user_2 = sample_user("user_2")
        self.user_3 = sample_user("user_3")
        self.user_4 = sample_user("user_4")
        self.user_5 = sample_user("user_5")

    def create_bid(self, user, tokens, bidding_price):
        """Create Bid object"""
        return models.Bid.objects.create(
            coin=self.coin,
            user=user,
            number_of_tokens=tokens,
            bidding_price=bidding_price,
        )

    def create_bids(self):
        """Create user bids"""
        self.user_1_bid = self.create_bid(self.user_1, 10, 30000)
        self.user_2_bid = self.create_bid(self.user_2, 10, 29000)
        self.user_3_bid = self.create_bid(self.user_3, 6, 15000)
        self.user_4_bid = self.create_bid(self.user_4, 5, 15000)
        self.user_5_bid = self.create_bid(self.user_5, 2, 2000)

    @patch('core.models.current_date')
    def test_send_token(self, mock_return):
        """Test send token"""
        mock_return.return_value = \
            utils.current_date() - timedelta(days=10)

        self.coin.bidding_window = utils.current_date()

        self.coin.save()
        self.coin.refresh_from_db()

        send_tokens()

        self.user_1_bid.refresh_from_db()
        self.user_2_bid.refresh_from_db()
        self.user_3_bid.refresh_from_db()
        self.user_4_bid.refresh_from_db()
        self.user_5_bid.refresh_from_db()

        self.assertEquals(
            self.user_1_bid.token_recieved,
            self.user_1_bid.number_of_tokens)
        self.assertEquals(
            self.user_2_bid.token_recieved,
            self.user_2_bid.number_of_tokens)
        self.assertEquals(
            self.user_3_bid.token_recieved,
            self.user_3_bid.number_of_tokens)
        self.assertEquals(
            self.user_4_bid.token_recieved,
            2.00000)
        self.assertEquals(
            self.user_5_bid.token_recieved,
            None)

        self.assertEquals(
            self.user_1_bid.status,
            'recieved all')
        self.assertEquals(
            self.user_2_bid.status,
            'recieved all')
        self.assertEquals(
            self.user_3_bid.status,
            'recieved all')
        self.assertEquals(
            self.user_4_bid.status,
            'recieved some')
        self.assertEquals(
            self.user_5_bid.status,
            'None')

    def test_bidding_window(self):
        """
        Test token are not sent until
        bidding window is closed
        """

        send_tokens()

        self.user_1_bid.refresh_from_db()
        self.user_2_bid.refresh_from_db()
        self.user_3_bid.refresh_from_db()
        self.user_4_bid.refresh_from_db()
        self.user_5_bid.refresh_from_db()

        self.assertEquals(
            self.user_1_bid.token_recieved,
            None)
        self.assertEquals(
            self.user_2_bid.token_recieved,
            None)
        self.assertEquals(
            self.user_3_bid.token_recieved,
            None)
        self.assertEquals(
            self.user_4_bid.token_recieved,
            None)
        self.assertEquals(
            self.user_5_bid.token_recieved,
            None)

        self.assertEquals(
            self.user_1_bid.status,
            'None')
        self.assertEquals(
            self.user_2_bid.status,
            'None')
        self.assertEquals(
            self.user_3_bid.status,
            'None')
        self.assertEquals(
            self.user_4_bid.status,
            'None')
        self.assertEquals(
            self.user_5_bid.status,
            'None')
