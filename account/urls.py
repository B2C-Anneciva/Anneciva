from django.urls import path

from account.views import RegistrationAPIView, UserLoginView, UserProfileView, ChangePasswordView, EditProfileView, \
    SendPasswordEmailView, UserPasswordResetView, VerificationView, LogoutView


urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('verify/<uid>/<token>/', VerificationView.as_view(), name='verify'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('edit_profile/<int:pk>/', EditProfileView.as_view(), name='edit_profile'),
    path('send-reset-password/', SendPasswordEmailView.as_view(), name='send-reset-password'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='password-reset'),
]
