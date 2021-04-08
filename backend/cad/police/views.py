from rest_framework import viewsets
from django.contrib.auth.models import Group
from . import models
from . import serializers
from common.views import GroupPermsModelViewSet


class RankViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Rank.objects.all().order_by('-id')
    serializer_class = serializers.RankSerializer


class CallViewSet(GroupPermsModelViewSet):
    model = models.Call
    serializer_class = serializers.CallSerializer
    required_groups = {
        'GET': ['Police', 'ApiAdmin'],
        'PUT': ['Supervisor', 'ApiAdmin', '__owner__'],
        'POST': ['Police', 'ApiAdmin'],
        'DELETE': ['Supervisor', 'ApiAdmin', '__owner__']
    }


class OfficerViewSet(GroupPermsModelViewSet):
    model = models.Officer
    serializer_class = serializers.OfficerSerializer
    required_groups = {
        'GET': ['Police', 'ApiAdmin'],
        'PUT': ['Supervisor', 'ApiAdmin', '__owner__'],
        'POST': ['Supervisor', 'ApiAdmin'],
        'DELETE': ['Supervisor', 'ApiAdmin']
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # Add police group to user
        police_group = Group.objects.get(name='Police')
        if police_group:
            self.request.user.groups.add(police_group)
