from rest_framework import serializers
from . import models


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    #user = serializers.HyperlinkedRelatedField(
        #view_name='user-detail', read_only=True)

    class Meta:
        model = models.Character
        fields = ['url', 'first_name', 'last_name', 'height', 'weight', 'image',
                  'hair_color', 'eye_color', 'user', 'sex', 'race', 'dob', 'is_deceased']


class EyeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EyeColor
        fields = ['url', 'name']


class HairColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.HairColor
        fields = ['url', 'name']


class RaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Race
        fields = ['url', 'name', 'abbreviation']


class SexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Sex
        fields = ['url', 'name', 'abbreviation']
