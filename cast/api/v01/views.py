from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET',])
def index(request):
    # movies = Movie.objects.all()
    # serialized_movies = MovieSerializer(instance=movies, many=True)
    # return Response(data=serialized_movies.data,status=status.HTTP_400_BAD_REQUEST)
    pass

@api_view(['POST',])
def create(request):
    data = {"message": "Movie created successfully "}
    return Response(data=data,status=status.HTTP_201_CREATED)

@api_view(['GET',])
def show(request,id):
    data = {"message": "Movie Details "}
    return Response(data=data,status=status.HTTP_302_FOUND)

@api_view(['PUT',])
def update(request,id):
    data = {"message": "Movie updated successfully "}
    return Response(data=data,status=status.HTTP_200_OK)
    
@api_view(['PATCH',])
def updatev2(request,id):
    data = {"message": "Movie updated successfully "}
    return Response(data=data,status=status.HTTP_200_OK)
 
@api_view(['DELETE',])
def destroy(request,id):
    data = {"message": "Movie Deleted successfully "}
    return Response(data=data,status=status.HTTP_200_OK)

