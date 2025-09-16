from rest_framework import serializers
from .models import VehicleDetails

class VehicleDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetails
        fields = '__all__'