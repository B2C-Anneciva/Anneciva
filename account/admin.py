from django.contrib import admin
from account.models import CustomerUser

@admin.register(CustomerUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email' , 'user_type')
    search_fields = ('user_type', 'full_name', 'email')