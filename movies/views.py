from django.shortcuts import render, get_object_or_404
from .models import Movie, Show

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})


def show_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    shows = Show.objects.filter(movie=movie)
    return render(request, 'show_list.html', {
        'movie': movie,
        'shows': shows
    })
