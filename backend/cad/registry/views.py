from rest_framework import serializers, viewsets
from . import models
from . import serializers
from common.views import GroupPermsModelViewSet


class VehicleColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.VehicleColor.objects.all().order_by('-id')
    serializer_class = serializers.VehicleColorSerializer


class VehicleTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.VehicleType.objects.all().order_by('-id')
    serializer_class = serializers.VehicleTypeSerializer


class VehicleMakeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.VehicleMake.objects.all().order_by('-id')
    serializer_class = serializers.VehicleMakeSerializer


class VehicleViewSet(GroupPermsModelViewSet):
    model = models.Vehicle
    serializer_class = serializers.VehicleSerializer
    required_groups = required_groups = {
        'GET': ['Police', 'ApiAdmin', '__owner__'],
        'POST': ['__all__'],
        'PUT': ['ApiAdmin', '__owner__'],
        'DELETE': ['ApiAdmin', '__owner__']
    }

    def perform_create(self, serializer):
        serializer.save(character=self.request.character)


class WeaponTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.WeaponType.objects.all().order_by('-id')
    serializer_class = serializers.WeaponTypeSerializer


class WeaponViewSet(GroupPermsModelViewSet):
    model = models.Weapon
    serializer_class = serializers.WeaponSerializer
    required_groups = required_groups = {
        'GET': ['Police', 'ApiAdmin', '__owner__'],
        'POST': ['__all__'],
        'PUT': ['ApiAdmin', '__owner__'],
        'DELETE': ['ApiAdmin', '__owner__']
    }

    def perform_create(self, serializer):
        serializer.save(character=self.request.character)


class LicenseTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.LicenseType.objects.all().order_by('-id')
    serializer_class = serializers.LicenseTypeSerializer


class LicenseStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.LicenseStatus.objects.all().order_by('-id')
    serializer_class = serializers.LicenseStatusSerializer


class LicenseViewSet(GroupPermsModelViewSet):
    model = models.License
    serializer_class = serializers.LicenseSerializer
    required_groups = required_groups = {
        'GET': ['Police', 'ApiAdmin', '__owner__'],
        'POST': ['__all__'],
        'PUT': ['ApiAdmin', '__owner__'],
        'DELETE': ['ApiAdmin', '__owner__']
    }

    def perform_create(self, serializer):
        serializer.save(character=self.request.character)
