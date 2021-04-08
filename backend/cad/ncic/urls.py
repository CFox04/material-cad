from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'arrests', views.ArrestViewSet, basename='arrest')
router.register(r'charge_types', views.ChargeTypeViewSet)
router.register(r'charges', views.ChargeViewSet, basename='charge')
router.register(r'flag_types', views.FlagTypeViewSet)
router.register(r'flag', views.FlagViewSet, basename='flag')
router.register(r'warrant_types', views.WarrantTypeViewSet)
router.register(r'warrants', views.WarrantViewSet, basename='warrant')
router.register(r'vehicle_citation_reasons',
                views.VehicleCitationReasonViewSet)
router.register(r'vehicle_citations', views.VehicleCitationViewSet, basename='vehicle_citation')
router.register(r'citation_reasons', views.CitationReasonViewSet)
router.register(r'citations', views.CitationViewSet, basename='citation')
router.register(r'bolos', views.BoloViewSet, basename='bolo')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
