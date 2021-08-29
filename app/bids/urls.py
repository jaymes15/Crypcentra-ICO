from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('review', views.ReviewBidsViewSet,
                basename="bids_review")
router.register('', views.BidsViewSet,
                basename="bids")


app_name = 'bids'

urlpatterns = [
    path('', include(router.urls)),
]
