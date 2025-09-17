from rest_framework import serializers
from .models import VehicleDetails, OTPDetails

class VehicleDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetails
        fields = '__all__'

class otpSerializer(serializers.ModelSerializer):
    class Meta:
        model =   OTPDetails
        fields = '__all_'      