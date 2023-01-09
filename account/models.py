from django.db import models
# from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
import random

class User(models.Model):
    PC_CHOICE = (
        ('PROVIDER', 'provider'),
        ('COSTUMER', 'customer'),
        ('BOTH', 'both'),
    )
    email = models.EmailField(
        max_length=100,
        unique=True
    )
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)
    country = CountryField()
    company_name = models.CharField(max_length=255, null=True, blank=True)
    pc = models.CharField(max_length=10, null=True, choices=PC_CHOICE)
    phone_number = models.CharField(max_length=50, unique=True)
    corporate_number = models.CharField(max_length=50, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone_number"]
    def __str__(self):
        return f'{self.username}'
