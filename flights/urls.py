from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("airp/", views.airp, name="airp"),
    path("<int:flight_id>", views.flight, name="flight")
]