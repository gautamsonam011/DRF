from .models import VehicleDetails
from rest_framework import serializers


class VehicleDetailsSerializer(serializers.ModelSerializer):
    class Meta:

        modes = VehicleDetails
        fields = '__all__'
 