from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# Import routers from other apps
# from user.urls import router as user_router
from civilian.urls import router as civilian_router
from registry.urls import router as registry_router
from police.urls import router as police_router
from ncic.urls import router as ncic_router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

registries = [
    civilian_router.registry, registry_router.registry, police_router.registry, ncic_router.registry]

router = DefaultRouter()

for registry in registries:
    router.registry.extend(registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/user/', include('user.urls', namespace='user')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
