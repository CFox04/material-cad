from django.db import models
from registry.models import EnumModel


class Rank(EnumModel):
    pass


class Call(models.Model):
    caller = models.ForeignKey("civilian.Character", on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=100)


class Officer(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    attached_call = models.ForeignKey(
        Call, null=True, on_delete=models.SET_NULL)
    rank = models.ForeignKey(Rank, null=True, on_delete=models.SET_NULL)
    date_joined = models.DateField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return f"{self.user.username}"
