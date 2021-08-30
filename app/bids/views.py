from rest_framework import viewsets, mixins, \
    permissions
from core.models import Bid
from bids import serializers


class BidsViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  ):
    """Bids endpoint"""

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
        serializer.save(user=self.request.user)


class ReviewBidsViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        ):
    """Review Bids endpoint"""

    permission_classes = (permissions.IsAuthenticated,)

    queryset = Bid.objects.all()
    serializer_class = serializers.BidListSerializer

    def get_queryset(self):
        return Bid.objects.filter(coin__owner=self.request.user)
