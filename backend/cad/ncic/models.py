from django.db import models
from registry.models import EnumModel

# Create your models here.


class Record(models.Model):
    character = models.ForeignKey(
        "civilian.Character", on_delete=models.CASCADE)
    officer = models.ForeignKey(
        "police.Officer", null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)


class Arrest(Record):
    location = models.CharField(max_length=100)
    witness_names = models.CharField(max_length=255)
    incident_summary = models.TextField()
    evidence_found = models.TextField()
    is_felony = models.BooleanField()
    is_gang_related = models.BooleanField()
    weapon_used = models.BooleanField()
    officer_used_force = models.BooleanField()

    def __str__(self):
        return f"{self.date}: {self.officer.user.username}"


class ChargeType(EnumModel):
    pass


class Charge(Record):
    related_arrest = models.ForeignKey(Arrest, on_delete=models.CASCADE)
    charge_type = models.ForeignKey(ChargeType, on_delete=models.CASCADE)


class FlagType(EnumModel):
    pass


class Flag(Record):
    flag_type = models.ForeignKey(FlagType, on_delete=models.CASCADE)


class WarrantType(EnumModel):
    pass


class Warrant(Record):
    warrant_type = models.ForeignKey(WarrantType, on_delete=models.CASCADE)


class VehicleCitationReason(EnumModel):
    pass


class VehicleCitation(Record):
    reason = models.ForeignKey(VehicleCitationReason, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=25)
    vehicle_type = models.ForeignKey(
        "registry.VehicleType", null=True, on_delete=models.SET_NULL)
    vehicle_make = models.ForeignKey(
        "registry.VehicleMake", null=True, on_delete=models.SET_NULL)
    vehicle_color = models.ForeignKey(
        "registry.VehicleColor", null=True, on_delete=models.SET_NULL)
    vehicle_speed = models.IntegerField(default=0)
    speed_limit = models.IntegerField(default=0)
    details = models.TextField()


class CitationReason(EnumModel):
    pass


class Citation(Record):
    reason = models.ForeignKey(CitationReason, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    details = models.TextField()


class Bolo(Record):
    description = models.CharField(max_length=25)
