from django.urls import path
from account.views import RegistrationAPIView, UserLoginView

# app_name = 'account'
urlpatterns = [
    path('register', RegistrationAPIView.as_view()),
    path('login', UserLoginView.as_view()),
]
