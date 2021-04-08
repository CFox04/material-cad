from rest_framework import serializers
from . import models


class RankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Rank
        fields = ['name']


class CallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Call
        fields = ['caller', 'description', 'location']


class OfficerSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.CharField(allow_blank=True)

    class Meta:
        model = models.Officer
        fields = ['user', 'attached_call',
                  'rank', 'date_joined', 'notes']
