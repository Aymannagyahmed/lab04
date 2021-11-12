from functools import partial
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer
from movie.models import Movie
from django.shortcuts import get_object_or_404

@api_view(['GET',])
def index(request):
    movies = Movie.objects.all()
    serialized_movies = MovieSerializer(instance=movies, many=True)
    return Response(data=serialized_movies.data,status=status.HTTP_200_OK)

@api_view(['POST',])
def create(request):
    serialized_movie = MovieSerializer(data=request.data)
    if serialized_movie.is_valid():
        serialized_movie.save()
        return Response(data=serialized_movie.data,status=status.HTTP_201_CREATED)
    return Response(data=serialized_movie.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def show(request,id):
    movie_obj = get_object_or_404(Movie,pk=id)
    serialized_movie = MovieSerializer(instance=movie_obj)
    return Response(data=serialized_movie.data,status=status.HTTP_302_FOUND)

@api_view(['PUT','PATCH'])
def update(request,id):
    movie_obj = get_object_or_404(Movie,pk=id)
    serialized_movie = MovieSerializer(data=request.data,instance=movie_obj,partial= request.method == 'PATCH')
    if serialized_movie.is_valid():
        serialized_movie.save()
        return Response(data=serialized_movie.data,status=status.HTTP_200_OK)
    return Response(data=serialized_movie.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def destroy(request,id):
    movie_obj = get_object_or_404(Movie,pk=id)
    movie_obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

