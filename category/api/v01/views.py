from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from category.models import Category
from .serializers import CategorySerializer


@api_view(['GET',])
def index(request):
    categores = Category.objects.all()
    serialized_category = CategorySerializer(instance=categores, many=True)
    return Response(data=serialized_category.data,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
def create(request):
    serialized_category = CategorySerializer(data=request.data)
    if serialized_category.is_valid():
        serialized_category.save()
        return Response(data=serialized_category.data,status=status.HTTP_201_CREATED)
    return Response(data=serialized_category.errors,status=status.HTTP_400_BAD_REQUEST)


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

