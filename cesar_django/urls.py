from django.contrib.auth.decorators import login_required
from django.urls import path, include

from cesar_django import views

app_name = "cesar_django"

urlpatterns = [
    path("get-crypto/", views.CryptoTextCreate.as_view(), name="get-crypto"),
]