from django.urls import path
from . import views

urlpatterns = [
    path("", views.quote_req, name="request"),
    path("show", views.QuoteList.as_view(), name="show"),
    path("show/<int:pk>", views.QuoteDetail.as_view(), name="detail"),
]


app_name = "quotes"
