from rest_framework import serializers
from .models import VehicleDetails, OTPDetails, ProfileDetails

class VehicleDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetails
        fields = '__all__'

class VehicleNameSerializer(serializers.ModelSerializer):
    model = VehicleDetails
    fields = ['vehicleName']        

class otpSerializer(serializers.ModelSerializer):
    class Meta:
        model =   OTPDetails
        fields = ['mobileNumber']      

class verifyOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTPDetails
        fields = ["mobileNumber", "otp"]  

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileDetails
        fields = '__all__'
                      