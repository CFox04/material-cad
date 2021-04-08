from rest_framework import viewsets
from . import models
from . import serializers
from common.views import GroupPermsModelViewSet

# With the exception of Police, ApiAdmin, or Superuser, only the owner of the character should be able to view said character.


class CharacterViewSet(GroupPermsModelViewSet):
    model = models.Character
    serializer_class = serializers.CharacterSerializer
    required_groups = required_groups = {
        'GET': ['Police', 'ApiAdmin', '__owner__'],
        'POST': ['__all__'],
        'PUT': ['ApiAdmin', '__owner__'],
        'DELETE': ['ApiAdmin', '__owner__']
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EyeColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.EyeColor.objects.all().order_by('-id')
    serializer_class = serializers.EyeColorSerializer


class HairColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.HairColor.objects.all().order_by('-id')
    serializer_class = serializers.HairColorSerializer


class RaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Race.objects.all().order_by('-id')
    serializer_class = serializers.RaceSerializer


class SexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Sex.objects.all().order_by('-id')
    serializer_class = serializers.SexSerializer
