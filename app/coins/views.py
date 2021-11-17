from rest_framework import mixins, permissions, viewsets
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings
from coins import serializers
from core.models import Coin


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class CoinsViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    """Coins endpoint"""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Coin.objects.all()
    serializer_class = serializers.CoinSerializer

    def get_serializer_class(self):

        if self.action == "list" or self.action == "retrieve":
            return serializers.CoinListSerializer

        return serializers.CoinSerializer

    def get_queryset(self):
        coin_name = self.request.query_params.get("coin_name", None)

        if self.request.user.is_authenticated:

            return Coin.objects.filter(owner=self.request.user)

        elif coin_name is None:

            return Coin.objects.all()

        else:
            return Coin.objects.filter(name=coin_name)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
