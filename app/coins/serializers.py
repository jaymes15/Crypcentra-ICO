from rest_framework import serializers
from core.models import Coin
from users.serializers import UserSerializer


class CoinListSerializer(serializers.ModelSerializer):
    """List Coin model serializer"""
    owner = UserSerializer(read_only=True)

    class Meta(object):
        model = Coin
        fields = ('id', 'owner', 'name', 'description',
                  'created_on', 'bidding_window',
                  'number_of_available_token')
        read_only_fields = ('id', 'owner', 'name', 'description',
                            'created_on', 'bidding_window',
                            'number_of_available_token')


class CoinSerializer(serializers.ModelSerializer):
    """Coin model serializer"""

    class Meta(object):
        model = Coin
        fields = ('id', 'owner', 'name', 'description',
                  'created_on', 'bidding_window',
                  'number_of_available_token')
        read_only_fields = ('id', 'owner', 'created_on',)
