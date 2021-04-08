from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'register', views.RegisterUser, basename="register")

app_name = 'user'

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name="register_user"),
]
