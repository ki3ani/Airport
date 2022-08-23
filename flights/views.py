from django.shortcuts import render
from .models import Flight,Airport,Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

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
        "passengers": flight.passengers.all(),
        "non-passengers": Passenger.objects.exclude(flights=flight).all()
    })

def flight(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return render( HttpResponseRedirect(reverse("flight", args=(flight.id))))
        
