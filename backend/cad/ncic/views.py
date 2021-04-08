from rest_framework import viewsets
from . import models
from . import serializers
from common.views import GroupPermsModelViewSet


class ArrestViewSet(GroupPermsModelViewSet):
    model = models.Arrest
    serializer_class = serializers.ArrestSerializer
    required_groups = {
        'GET': ['Police', 'ApiAdmin'],
        'PUT': ['Supervisor', 'ApiAdmin'],
        'POST': ['Police', 'ApiAdmin'],
        'DELETE': ['Supervisor', 'ApiAdmin']
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChargeTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.ChargeType.objects.all().order_by('-id')
    serializer_class = serializers.ChargeTypeSerializer


class ChargeViewSet(GroupPermsModelViewSet):
    model = models.Charge
    serializer_class = serializers.ChargeSerializer
    required_groups = {
        'GET': ['Police', 'ApiAdmin'],
        'PUT': ['Supervisor', 'ApiAdmin'],
        'POST': ['Police', 'ApiAdmin'],
        'DELETE': ['Supervisor', 'ApiAdmin', '__owner__']
    }


class FlagTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.FlagType.objects.all().order_by('-id')
    serializer_class = serializers.FlagTypeSerializer


class FlagViewSet(GroupPermsModelViewSet):
    model = models.Flag
    serializer_class = serializers.FlagSerializer
    required_groups = {
        'GET': ['Police', 'ApiAdmin'],
        'PUT': ['Police', 'ApiAdmin'],
        'POST': ['Police', 'ApiAdmin'],
        'DELETE': ['Supervisor', 'ApiAdmin', '__owner__']
    }


class WarrantTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.WarrantType.objects.all().order_by('-id')
    serializer_class = serializers.WarrantTypeSerializer


class WarrantViewSet(GroupPermsModelViewSet):
    model = models.Warrant
    serializer_class = serializers.WarrantSerializer
    required_groups = {
        'GET': ['Police', 'ApiAdmin'],
        'PUT': ['Supervisor', 'ApiAdmin'],
        'POST': ['Police', 'ApiAdmin'],
        'DELETE': ['Supervisor', 'ApiAdmin', '__owner__']
    }


class VehicleCitationReasonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.VehicleCitationReason.objects.all().order_by('-id')
    serializer_class = serializers.VehicleCitationReasonSerializer


class VehicleCitationViewSet(GroupPermsModelViewSet):
    model = models.VehicleCitation
    serializer_class = serializers.VehicleCitationSerializer
    required_groups = {
        'GET': ['Police', 'ApiAdmin'],
        'PUT': ['Police', 'ApiAdmin'],
        'POST': ['Police', 'ApiAdmin'],
        'DELETE': ['Supervisor', 'ApiAdmin', '__owner__'],
    }


class CitationReasonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CitationReason.objects.all().order_by('-id')
    serializer_class = serializers.CitationReasonSerializer


class CitationViewSet(GroupPermsModelViewSet):
    model = models.Citation
    serializer_class = serializers.CitationSerializer
    required_groups = {
        'GET': ['Police', 'ApiAdmin'],
        'PUT': ['Police', 'ApiAdmin'],
        'POST': ['Police', 'ApiAdmin'],
        'DELETE': ['Supervisor', 'ApiAdmin', '__owner__'],
    }


class BoloViewSet(GroupPermsModelViewSet):
    model = models.Bolo
    serializer_class = serializers.BoloSerializer
    required_groups = {
        'GET': ['Police', 'ApiAdmin'],
        'PUT': ['Police', 'ApiAdmin'],
        'POST': ['Police', 'ApiAdmin'],
        'DELETE': ['Supervisor', 'ApiAdmin', '__owner__'],
    }
