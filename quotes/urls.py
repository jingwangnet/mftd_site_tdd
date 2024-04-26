from django.urls import path
from . import views

urlpatterns = [
    path("", views.quote_req, name="request"),
]


app_name = "quotes"
