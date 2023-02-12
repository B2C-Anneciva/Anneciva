from django.shortcuts import render
from rest_framework import generics, permissions, status

from order.serializers import AddToCartSerializer, CartViewSerializer
from rest_framework.response import Response

from order.models import Order, OrderDetail
from account.models import CustomerUser
from product.models import Product


class AddToCartView(generics.ListAPIView, generics.CreateAPIView):

    serializer_class = AddToCartSerializer
    permission_classes = [permissions.AllowAny]
    queryset = OrderDetail.objects.all()

class CartView(generics.ListAPIView):

     serializer_class = CartViewSerializer
     queryset = CustomerUser.objects.all()

     def get(self, request, *args, **kwargs):

         pk = kwargs.get('pk', None)

         try:
             obj = CustomerUser.objects.get(id=pk)
         except OrderDetail.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)

         serializer = CartViewSerializer(obj)
         return Response(serializer.data)





