from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import VehicleDetails, OTPDetails

from .serializers import VehicleDetailsSerializer, otpSerializer
from rest_framework.views import APIView
import random

# Create your views here.

@api_view(['POST'])
def create_views_data(request):
    serializer = VehicleDetailsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def get_all_data(request):
    new_data = VehicleDetails.objects.all()

    serializer = VehicleDetailsSerializer(new_data, many=True)
    return Response(serializer.data)      

@api_view(['PUT'])
def update_record(request, pk ):
    new_data = VehicleDetails.objects.filter(pk=pk).first()

    if not new_data:
        return Response({'error': 'Vehicle not found'}, status = status.HTTP_404_NOT_FOUND)
    
    serializer = VehicleDetailsSerializer(new_data, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT', 'DELETE'])
def vehicle_details_op(request, pk):
    new_data = VehicleDetails.objects.filter(pk=pk).first()

    if not new_data:
        return Response({'error': 'Vehicle not found'}, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VehicleDetailsSerializer(new_data)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = VehicleDetailsSerializer(new_data, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        new_data.delete()
        return Response({'message':'Vehicle delete successfully!'},status = status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_views_otp(request):
    serializer = otpSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

def generate_otp(length = 6):
    return ''.join([str(random.randint(0,9)) for _ in range(length)])

class SendOTPView(APIView):

    def post(self, request):
        serializer = otpSerializer(data=request.data)

        if serializer.is_valid():
            mobileNumber = serializer.validated_data['mobileNumber']
            otp = generate_otp(6)

            # Save to database
            OTPDetails.objects.create(mobileNumber=mobileNumber, otp=otp)

            # Print the OTP for testing (in production, send via SMS)
            print(f"Generated OTP for {mobileNumber}: {otp}")

            return Response({'message': 'OTP sent successfully.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)















