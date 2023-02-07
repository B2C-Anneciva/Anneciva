from django.conf.urls.static import static, settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Avicenna API",
      default_version='v1',
      description="Swagger docs for REST API",
      contact=openapi.Contact("Avicenna <info@avicenna.uz>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/user/', include('account.urls')),
    path('product/pr/', include('product.urls')),
    path('api/token-obtain-pair-view/', TokenObtainPairView.as_view(), name='tokenobtainpairview'),
    path('api/refresh-token/', TokenRefreshView.as_view(), name='refreshtoken'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/api.json/', schema_view.without_ui( cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATICFILES_DIRS
)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
