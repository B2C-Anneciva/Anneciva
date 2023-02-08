from django.urls import path
from product.views import ProductView, ProductDetailView
from product import views

urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail')
]
