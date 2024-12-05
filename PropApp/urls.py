from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from PropApp import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("properties/", include("properties.urls")),
    path("api/v1/", include("api.urls")),
    path("", include("core.urls")),
    # localhost:8000/example
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # YOUR PATTERNS
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/v1/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
