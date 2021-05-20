from django.shortcuts import render
from django.views.generic import ListView, CreateView
from order.models import Order
class CreateOrderView(CreateView):
    model = Order
    fields= "__all__"
    template_name = "order_create.html"