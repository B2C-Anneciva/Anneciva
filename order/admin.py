from django.contrib import admin
from order.models import Order, OrderDetail

admin.site.register(Order)
@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')
    search_fields = ('user', 'product')