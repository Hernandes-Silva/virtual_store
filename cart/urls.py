from django.contrib import admin
from django.urls import path
from cart import views

urlpatterns = [
    path('add/<int:product_id>', views.cart_add, name="cart_add"),
    path('deatil/', views.cart_detail, name="cart_detail"),
]