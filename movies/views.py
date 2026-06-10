from django.shortcuts import render, get_object_or_404
from .models import Movie, Show
from accounts.models import Location  

def home(request):
    return render(request, "home.html")

def location_list(request):
    locations = Location.objects.all()
    return render(request, "location_selection.html", {
        "locations": locations
    })

def movie_list(request, location_id):
    location = get_object_or_404(Location, id=location_id)

    movies = Movie.objects.filter(
        show__location=location
    ).distinct()

    return render(request, "movie_list.html", {
        "movies": movies,
        "location": location
    })


def show_list(request, movie_id, location_id):
    movie = get_object_or_404(Movie, id=movie_id)
    location = get_object_or_404(Location, id=location_id)

    shows = Show.objects.filter(
        movie=movie,
        location=location
    )

    return render(request, "show_list.html", {
        "movie": movie,
        "shows": shows,
        "location": location
    })
