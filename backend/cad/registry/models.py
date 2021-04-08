from django.db import models
from django.apps import apps

class EnumModel(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

class VehicleColor(EnumModel):
    pass

class VehicleMake(EnumModel):
    pass

class VehicleType(EnumModel):
    pass

class Vehicle(models.Model):
    character = models.ForeignKey("civilian.Character", on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=25)
    vehicle_type = models.ForeignKey(VehicleType, null=True, on_delete=models.SET_NULL)
    vehicle_make = models.ForeignKey(VehicleMake, null=True, on_delete=models.SET_NULL)
    vehicle_color = models.ForeignKey(VehicleColor, null=True, on_delete=models.SET_NULL)


class WeaponType(EnumModel):
    pass

class Weapon(models.Model):
    character = models.ForeignKey("civilian.Character", on_delete=models.CASCADE)
    weapon_type = models.ForeignKey(WeaponType, on_delete=models.CASCADE)


class LicenseType(EnumModel):
    pass

class LicenseStatus(EnumModel):
    pass

class License(models.Model):
    character = models.ForeignKey("civilian.Character", on_delete=models.CASCADE)
    license_type = models.ForeignKey(LicenseType, on_delete=models.CASCADE)
    status = models.ForeignKey(LicenseStatus, null=True, on_delete=models.SET_NULL)