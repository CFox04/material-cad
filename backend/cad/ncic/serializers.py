from rest_framework import serializers
from . import models


class ArrestSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail', read_only=True)

    class Meta:
        model = models.Arrest
        fields = '__all__'


class ChargeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ChargeType
        fields = '__all__'


class ChargeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Charge
        fields = '__all__'


class FlagTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FlagType
        fields = '__all__'


class FlagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Flag
        fields = '__all__'


class WarrantTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.WarrantType
        fields = '__all__'


class WarrantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Warrant
        fields = '__all__'


class VehicleCitationReasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.VehicleCitationReason
        fields = '__all__'


class VehicleCitationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.VehicleCitation
        fields = '__all__'


class CitationReasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CitationReason
        fields = '__all__'


class CitationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Citation
        fields = '__all__'


class BoloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Bolo
        fields = '__all__'
