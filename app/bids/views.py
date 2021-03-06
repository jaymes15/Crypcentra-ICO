
from rest_framework import mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from bids import serializers
from core.models import Bid


class BidsViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    """Bids endpoint"""

    permission_classes = (permissions.IsAuthenticated,)

    queryset = Bid.objects.all()
    serializer_class = serializers.BidSerializer
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):

        if self.action == "list" or self.action == "retrieve":
            return serializers.BidListSerializer

        return serializers.BidSerializer

    def get_queryset(self):
        return Bid.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewBidsViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    """Review Bids endpoint"""

    permission_classes = (permissions.IsAuthenticated,)

    queryset = Bid.objects.all()
    serializer_class = serializers.BidListSerializer

    def get_queryset(self):
        return Bid.objects.filter(coin__owner=self.request.user)
