from django.urls import path
from . import views

urlpatterns = [
    path("", views.quote_req, name="request"),
    path("show", views.QuoteList.as_view(), name="show"),
]


app_name = "quotes"
