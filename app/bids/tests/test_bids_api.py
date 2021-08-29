from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Bid
from core.tests import utils
from bids.serializers import BidListSerializer,\
    BidSerializer
from core.helpers import sample_user


BIDS_URL = reverse('bids:bids-list')


class TestBidsView(TestCase):

    def setUp(self):

        self.user = sample_user()
        self.another_user = sample_user("another_user")
        self.client = APIClient()

    def test_post(self):
        """Test POST"""
        self.client.force_authenticate(user=self.user)

        coin = utils.create_coin(self.user)

        payload = {
            "coin": coin.id,
            "number_of_tokens": 12.5,
            "bidding_price": 1000,

        }
        response = self.client.post(BIDS_URL, data=payload)
        bid_query = Bid.objects.last()
        serializer = BidSerializer(bid_query,
                                   many=False)

        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED)
        self.assertEquals(response.data, serializer.data)

    def test_post_requires_user_authentication(self):
        """Test POST requires user authentication"""
        coin = utils.create_coin(self.user)

        payload = {
            "coin": coin.id,
            "number_of_tokens": 12.5,
            "bidding_price": 1000,

        }
        response = self.client.post(BIDS_URL, data=payload)

        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED)

    def test_get_user_bids(self):
        """Test GET user bids"""
        self.client.force_authenticate(user=self.user)
        utils.create_bid(self.user)

        response = self.client.get(BIDS_URL)
        user_bids = Bid.objects.filter(user=self.user.id)
        serializer = BidListSerializer(user_bids, many=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)
        self.assertEquals(serializer.data, response.data)

    def test_get_requires_user_authentication(self):
        """Test GET requires user authentication"""
        utils.create_bid(self.user)

        response = self.client.get(BIDS_URL)

        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED)
