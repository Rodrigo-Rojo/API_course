from django.shortcuts import render
from django.http import JsonResponse
from django.urls import path


from .models import Movie


# Create your views here.
def index(request):
    all_movies = Movie.objects.all()
    data = {'movies': list(all_movies.values())}
    return JsonResponse(data)


def get_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
            'id': movie.id,
            'name': movie.name,
            'description': movie.description,
            'active': movie.active
    }
    return JsonResponse(data)
