from rest_framework import serializers
from order.models import Order, OrderDetail
from account.models import CustomerUser

class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = [
            'user',
            'product',
            'quantity',
        ]

class CartViewSerializer(serializers.ModelSerializer):

    details = AddToCartSerializer(many=True)
    class Meta:
        model = CustomerUser
        fields = [
            'id',
            'details',
        ]