from django.shortcuts import render
from .models import Flight,Airport,Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights":Flight.objects.all()
    })

def airp(request):
    return render(request, "flights/airp.html", {
        "airports": Airport.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk = flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    })