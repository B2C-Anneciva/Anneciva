from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import CustomerUser

@admin.register(CustomerUser)
class CustomerUserAdmin(UserAdmin):
    # readonly_fields = ('username', 'email', 'password', 'country', 'company_name', 'user_type', 'phone_number', 'corporate_number')
    list_display = ('username', 'email')