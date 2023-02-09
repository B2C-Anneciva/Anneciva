from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from product.models import Product, Category, Comment
from product.serializers import ProductSerializer, CategorySerializer, CommentSerializer, ProductDetailSerializer
from rest_framework.pagination import PageNumberPagination

class CategoryView(generics.ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class ProductView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category_id', 'name', 'country']
    search_fields = ['name']
    pagination_class = PageNumberPagination

class ProductDetailView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            obj = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductDetailSerializer(obj)
        return Response(serializer.data)

class CommentView(generics.ListAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        comment = CommentSerializer(data=request.data)
        if request.user.is_authenticated:
            if comment.is_valid():
                comment.save()
        return Response(status=status.HTTP_200_OK)



