from django.db import models
from registry.models import EnumModel

# Create your models here.


class HairColor(EnumModel):
    pass


class EyeColor(EnumModel):
    pass


class Race(EnumModel):
    abbreviation = models.CharField(null=True, max_length=25)


class Sex(EnumModel):
    abbreviation = models.CharField(null=True, max_length=25)


class Character(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    height = models.FloatField()
    weight = models.IntegerField()
    image = models.ImageField(null=True, upload_to="character_images/")
    hair_color = models.ForeignKey(
        HairColor, blank=False, null=True, on_delete=models.SET_NULL)
    eye_color = models.ForeignKey(
        EyeColor, blank=False, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex, blank=False, null=True,
                            on_delete=models.SET_NULL)
    race = models.ForeignKey(
        Race, blank=False, null=True, on_delete=models.SET_NULL)
    dob = models.DateField()
    is_deceased = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"
