from django.urls import path
from account.views import RegistrationAPIView, UserLoginView

# app_name = 'account'
urlpatterns = [
    path('home', RegistrationAPIView.as_view()),
    path('home2', RegistrationAPIView.as_view()),
]
