from django.db.models import query
from rest_framework import serializers
from . import models


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VehicleType
        fields = ['name']


class VehicleColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VehicleColor
        fields = ['name']


class VehicleMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VehicleMake
        fields = ['name']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.HyperlinkedRelatedField(
        view_name='civilian.character-detail', read_only=True)

    class Meta:
        model = models.Vehicle
        fields = ['character', 'license_plate', 'vehicle_type',
                  'vehicle_make', 'vehicle_color']


class WeaponTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WeaponType
        fields = ['name']


class WeaponSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.HyperlinkedRelatedField(
        view_name='civilian.character-detail', read_only=True)

    class Meta:
        model = models.Weapon
        fields = ['character', 'weapon_type']


class LicenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LicenseType
        fields = ['name']


class LicenseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LicenseStatus
        fields = ['name']


class LicenseSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.HyperlinkedRelatedField(
        view_name='civilian.character-detail', read_only=True)

    class Meta:
        model = models.License
        fields = ['character', 'license_type', 'status']
