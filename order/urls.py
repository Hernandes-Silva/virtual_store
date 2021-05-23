from django.contrib import admin
from django.urls import path
from order import views
app_name = 'order'
urlpatterns = [
    path('order/create', views.CreateOrderView.as_view(), name="order_create"),
]