from django.urls import path
from account.views import RegistrationAPIView

# app_name = 'account'
urlpatterns = [
    path('home', RegistrationAPIView.as_view()),
]
