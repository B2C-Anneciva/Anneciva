from django.contrib import admin
from account.models import CustomerUser

# admin.site.register(CustomerUser)
@admin.register(CustomerUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email' , 'user_type')
    search_fields = ('user_type', 'username', 'email')