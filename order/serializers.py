from xml.dom import ValidationErr

from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from order.models import Order, OrderDetail
from account.models import CustomerUser
from product.models import Product

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            # "quantity",
            "price",
            "image",
        )


class CartItemSerializer(serializers.ModelSerializer):

    product = CartProductSerializer()
    sub_total = serializers.SerializerMethodField(method_name='total_price')
    # grand_total = serializers.SerializerMethodField(method_name='main_total')

    class Meta:
        model = OrderDetail
        fields = ['id', 'quantity', 'product', 'sub_total']

    def total_price(self, cartitem: OrderDetail):
        return cartitem.total_price()

    # def main_total(self, cart: OrderDetail):
    #
    #     items = cart.orders.all()
    #     total = sum([item.quantity * item.product.price for item in items])
    #     return total



class CartItemAddSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField()

    class Meta:
        model = OrderDetail
        fields = [
            'product_id'
        ]


