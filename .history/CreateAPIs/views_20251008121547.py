from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import VehicleDetails, OTPDetails, ProfileDetails

from .serializers import VehicleDetailsSerializer, otpSerializer, verifyOTPSerializer, profileSerializer
from rest_framework.views import APIView
import random
from django.conf import settings
import requests


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
    
class VerifyOTPView(APIView):
    def post(self, request):
        serializer = verifyOTPSerializer(data=request.data)

        if serializer.is_valid():
            mobileNumber = serializer.validated_data['mobileNumber']
            otp = serializer.validated_data['otp']


            try:
                otp_record = OTPDetails.objects.get(mobileNumber=mobileNumber, otp=otp)
            except OTPDetails.DoesNotExist:
                return Response({'error': 'Invalid otp'})

            # if  otp_record.is_verified:
            #     return Response({'message': 'mobile already verified'})
            
            # if otp_record.is_expired():
            #     return Response({'error': 'otp expired'})
            
            otp_record.mobileNumberVerified = True
            otp_record.save()


            return Response({'message': 'mobile number verified successfully'})

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        

   

# class ProfileAPI(APIView):

#     def get(self, request):
#         profiles = ProfileDetails.objects.all()
#         serializer = profileSerializer(profiles, many = True, context = {'request': request})

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = profileSerializer(data = request.data, context = {'request': request})

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)  
#         return render(request, 'profile.html', {'title': 'Profile Manager'})   
# 
 
def postProfile(request):
    if request.method == 'POST':
        serializer = profileSerializer(data=request.POST, files=request.FILES, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return to the form page with errors
        return render(request, 'profile.html', {
            'title': 'Profile Manager',
            'errors': serializer.errors
        })

    return render(request, 'profile.html', {'title': 'Profile Manager'})   



# Google map API 
def google_map_view(request):
    return render(request, 'map.html', {'google_maps_api_key': 'AIzaSyD3cIEc-LZsC5hjVgpcmnmO3c3Y97m3wcE'})


    
def my_google_map_view(request):
    return render(request, 'map.html', {'GOOGLE_MAPS_API_KEY':settings.GOOGLE_MAPS_API_KEY})

# def weather_api_view(request):
#     city = request.GET.get("city", "Kanpur")
#     api_key = settings.WEATHER_API_KEY
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

#     response = requests.get(url)
#     data = response.json() if response.status_code == 200 else None
#     return render(request, "weather.html", {"weather_data": data, "city": city})

def weather_api_view(request):
    city = request.GET.get("city", "Kanpur")

    # --- WeatherAPI.com call ---
    weather_url = f"http://api.weatherapi.com/v1/current.json?key={settings.WEATHER_API_KEY}&q={city}&aqi=no"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json() if weather_response.status_code == 200 else None

    # --- OnceHub API call ---
    oncehub_url = "https://api.oncehub.com/v2/test"
    headers = {
        "accept": "application/json",
        "API-Key": settings.ONCEHUB_API_KEY
    }
    oncehub_response = requests.get(oncehub_url, headers=headers)
    oncehub_data = oncehub_response.json() if oncehub_response.status_code == 200 else None

    # --- Render template with both datasets ---
    return render(request, "weather.html", {
        "weather_data": weather_data,
        "oncehub_data": oncehub_data,
        "city": city
    })



# INSERT INTO VehicleDetails(
#     VehicleName, 
#     vehicleCategory,
#     vehicleBrand,
#     vehicleNumber,
#     vehicleColor,
#     vehicleManu,
#     vehiclePrice
#     )
# VALUES("ACE", "Bike", "BHN", "758694", "Black", "2024", "100000");

# Select vehicleName, vehicleCategory, vehiclePrice 
# From VehicleDetails;

# 1:- Removing Duplicate Code 

def get_user_full_name(user):
    return f"{user.first_name} {user.last_name}"

def get_author_full_name(author):
    return f"{author.first_name} {author.last_name}"



















