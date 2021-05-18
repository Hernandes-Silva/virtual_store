from django.contrib import admin
from django.urls import path
from cart import views

urlpatterns = [
    path('add/<int:product_id>', views.cart_add, name="cart_add"),
    path('detail/', views.cart_detail, name="cart_detail"),
    path('remove/', views.cart_remove, name="cart_remove"),
]