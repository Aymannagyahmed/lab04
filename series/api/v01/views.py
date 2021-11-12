from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET',])
def index(request):
    data = {"message": "Hello, world!"}
    return Response(data=data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def create(request):
    data = {"message": "Series created successfully "}
    return Response(data=data,status=status.HTTP_201_CREATED)

@api_view(['GET',])
def show(request,id):
    data = {"message": "Series Details "}
    return Response(data=data,status=status.HTTP_302_FOUND)

@api_view(['PUT',])
def update(request,id):
    data = {"message": "Series updated successfully "}
    return Response(data=data,status=status.HTTP_200_OK)
    
@api_view(['PATCH',])
def updatev2(request,id):
    data = {"message": "Series updated successfully "}
    return Response(data=data,status=status.HTTP_200_OK)
 
@api_view(['DELETE',])
def destroy(request,id):
    data = {"message": "Series Deleted successfully "}
    return Response(data=data,status=status.HTTP_200_OK)

