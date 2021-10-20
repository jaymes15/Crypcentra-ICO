from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("", views.CoinsViewSet, basename="coins")


app_name = "coins"

urlpatterns = [
    path("", include(router.urls)),
]
