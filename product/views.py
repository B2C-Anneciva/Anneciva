from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers import ProductSerializer

class ProductView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class ProductDetailView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            obj = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(obj)
        return Response(serializer.data)
