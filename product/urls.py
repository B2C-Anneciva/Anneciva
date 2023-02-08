from django.urls import path
from product.views import ProductView, ProductDetailView, CategoryView
from product import views

urlpatterns = [
    path('category', CategoryView.as_view(), name='category'),
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail')
]
