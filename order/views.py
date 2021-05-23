from order.forms import OrderForm
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from order.models import Order
from order.forms import OrderForm
class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "order_create.html"