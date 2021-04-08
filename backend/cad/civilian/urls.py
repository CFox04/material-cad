from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'characters', views.CharacterViewSet, basename='character')
router.register(r'hair_colors', views.HairColorViewSet)
router.register(r'eye_colors', views.EyeColorViewSet)
router.register(r'races', views.RaceViewSet)
router.register(r'sexes', views.SexViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
