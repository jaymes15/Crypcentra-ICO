from rest_framework import serializers
from core.models import Bid
from users.serializers import UserSerializer
from coins.serializers import CoinListSerializer


class BidListSerializer(serializers.ModelSerializer):
    """List Bid model serializer"""

    user = UserSerializer(read_only=True)
    coin = CoinListSerializer(read_only=True)

    class Meta(object):
        model = Bid
        fields = (
            "id",
            "coin",
            "user",
            "number_of_tokens",
            "bidding_price",
            "token_recieved",
            "status",
            "timestamp",
        )
        read_only_fields = (
            "id",
            "coin",
            "user",
            "number_of_tokens",
            "bidding_price",
            "token_recieved",
            "status",
            "timestamp",
        )


class BidSerializer(serializers.ModelSerializer):
    """Bid model serializer"""

    class Meta(object):
        model = Bid
        fields = (
            "id",
            "coin",
            "user",
            "number_of_tokens",
            "bidding_price",
            "token_recieved",
            "status",
            "timestamp",
        )
        read_only_fields = ("id", "user", "token_recieved",
                            "status", "timestamp")
