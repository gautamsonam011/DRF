from django.db import models

# Create your models here.


# Here create a vehicle details 

class VehicleDetails(models.Model):
    vehicleName = models.CharField(max_length = 200)
    vehicleCategory = models.CharField(max_length = 200)
    vehicleBrand = models.CharField(max_length=200)
    vehicleNumber = models.CharField(max_length=10)
    vehicleColor = models.CharField(max_length=10)
    vehicleManu = models.DateField(null = True)
    vehiclePrice = models.FloatField(null = True)

    def __str__(self):
        return self.vehicleName  



class OTPDetails(models.Model):
    opt = models.CharField(max_length=6)
    mobileNumber = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    mobileNumberVerified = models.BooleanField(default = False)
