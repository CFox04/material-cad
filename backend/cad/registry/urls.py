from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'vehicles', views.VehicleViewSet, basename='vehicle')
router.register(r'vehicle_colors', views.VehicleColorViewSet)
router.register(r'vehicle_types', views.VehicleTypeViewSet)
router.register(r'vehicle_makes', views.VehicleMakeViewSet)
router.register(r'weapons', views.WeaponViewSet, basename='weapon')
router.register(r'weapon_types', views.WeaponTypeViewSet)
router.register(r'licenses', views.LicenseViewSet, basename='license')
router.register(r'license_types', views.LicenseTypeViewSet)
router.register(r'license_statuses', views.LicenseStatusViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
