from django.db import models
from account.models import CustomerUser
from product.models import Product

class Order(models.Model):

    STATUSES = [
        ('PENDING', 'pending'),
        ('INPROGRESS', 'inprogress'),
        ('COMPLATED', 'complated'),
        ('CANCELED', 'canceled')
    ]

    customer = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, null=True, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    expired_date = models.DateTimeField(null=True)
    required_date = models.DateTimeField(null=True)
    shipped_date = models.DateTimeField(null=True)
    canceled_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, choices=STATUSES, default='PENDING')

    def __str__(self):
        return f'{self.customer.__str__()} -> order:{self.id}'

class OrderDetail(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='orders')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'order:{self.order.id} - {self.product}, quantity:{self.quantity}'


