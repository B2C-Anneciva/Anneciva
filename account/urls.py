from django.urls import path

from account.views import RegistrationAPIView, UserLoginView, UserProfileView, ChangePasswordView, EditProfileView, \
    SendPasswordEmailView, UserPasswordResetView, VerificationView

# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('verify/<uid>/<token>/', VerificationView.as_view(), name='verify'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('edit_profile/<int:pk>/', EditProfileView.as_view(), name='edit_profile'),
    path('send-reset-password/', SendPasswordEmailView.as_view(), name='send-reset-password'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='password-reset'),
    # path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('^redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
