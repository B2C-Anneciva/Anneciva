from django.urls import path
from order import views
urlpatterns = [
    path('cart/', views.CartItemView.as_view(), name="cart"),
    path('cart/add/', views.CartItemAddView.as_view()),
    path('cart/delete/<int:pk>/', views.CartItemDelView.as_view()),
    path('cart/add_one/<int:pk>/', views.CartItemAddOneView.as_view()),
    path('cart/reduce_one/<int:pk>/', views.CartItemReduceOneView.as_view()),
]