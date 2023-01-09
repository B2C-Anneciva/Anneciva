from django.urls import path
from account.views import RegistrationAPIView

urlpatterns = [
    path('home', RegistrationAPIView.as_view()),
]
