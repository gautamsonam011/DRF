from .models import VehicleDetails
from rest_framework import serializers


class VehicleDetailsSerializer(serializers.ModelSerializer):
    class Meta:

        modes = VehicleDetails
        fields = '__all__'

        # if you want to customise some fields 

        # fields = ['vehicleName', 'vehicleBrand', 'vehicleCategory']


 