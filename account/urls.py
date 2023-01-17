from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.views import RegistrationAPIView, UserLoginView, UserProfileView, ChangePasswordView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]
