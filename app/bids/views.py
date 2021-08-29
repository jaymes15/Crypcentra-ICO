from rest_framework import viewsets, mixins, \
    permissions, authentication
from core.models import Bid
from bids import serializers


class BidsViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  ):
    """Coins endpoint"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Bid.objects.all()
    serializer_class = serializers.BidSerializer

    def get_serializer_class(self):

        if self.action == 'list' or self.action == 'retrieve':
            return serializers.BidListSerializer

        return serializers.BidSerializer

    def get_queryset(self):
        return Bid.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
