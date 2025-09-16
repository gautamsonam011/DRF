from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import VehicleDetails
from .serializers import VehicleDetailsSerializer

# Create your views here.

@api_view(['POST'])
def create_views_data(request):
    serializer = VehicleDetailsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.data, status = status.HTTP_400_REQUEST)    

