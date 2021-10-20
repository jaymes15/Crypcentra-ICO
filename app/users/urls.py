from django.urls import path
from knox import views as knox_views
from .views import RegisterAPI, LoginAPI

app_name = "users"

urlpatterns = [
    path("token/", LoginAPI.as_view(), name="token"),
    path("logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("logoutall/", knox_views.LogoutAllView.as_view(), name="logoutall"),
    path("", RegisterAPI.as_view(), name="create"),
]
