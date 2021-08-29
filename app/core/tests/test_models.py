from django.test import TestCase
from django.db.utils import IntegrityError
from core import models
from core.tests import utils
from core.helpers import sample_user


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

    def test_str_return(self):
        """Test CoinModel str method"""

        coin = utils.create_coin(self.user)
        coin_query = models.Coin.objects.last()

        self.assertEquals(str(coin_query), str(coin))
