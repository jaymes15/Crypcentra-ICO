from rest_framework import viewsets, mixins, \
    permissions, authentication
from core.models import Coin
from coins import serializers


class CoinsViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   ):
    """Coins endpoint"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Coin.objects.all()
    serializer_class = serializers.CoinSerializer

    def get_serializer_class(self):

        if self.action == 'list' or self.action == 'retrieve':
            return serializers.CoinListSerializer

        return serializers.CoinSerializer

    def get_queryset(self):
        coin_name = self.request.query_params.get('coin_name', None)

        if self.request.user.is_authenticated:

            return Coin.objects.filter(owner=self.request.user)

        elif coin_name is None:

            return Coin.objects.all()

        else:
            return Coin.objects.filter(name=coin_name)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
