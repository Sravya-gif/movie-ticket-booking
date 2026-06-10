from django.shortcuts import render
from movies.models import Location

def home(request):
    locations = Location.objects.all()
    print(locations)  
    return render(request, "home.html", {
        "locations": locations
    })
