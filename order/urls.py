from django.urls import path
from order.views import AddToCartView, CartView
urlpatterns = [
    path('addcart/', AddToCartView.as_view(), name='addcart'),
    path('addcart/<int:pk>/', CartView.as_view(), name='cart'),
]