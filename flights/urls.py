from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("airp/", views.airp, name="airp")
]