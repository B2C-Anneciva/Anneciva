
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.views import RegistrationAPIView, UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/user/', include('account.urls')),
    path('api/token-obtain-pair-view/', TokenObtainPairView.as_view(), name='tokenobtainpairview'),
    path('api/refresh-token/', TokenRefreshView.as_view(), name='refreshtoken'),
]
