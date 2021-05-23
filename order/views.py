from products.models import Product
from order.forms import OrderForm
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import ListView, CreateView
from order.models import Order, Item
from cart.cart import Cart
from order.forms import OrderForm


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    def form_valid(self, form):
        cart = Cart(self.request)
        if cart:
            order = form.save()
            for item in cart:
                Item.objects.create(
                    order=order,
                    product = item['product'],
                    price = item['price'],
                    quantity = item['quantity']
                )
                product = Product.objects.get(pk=item['product']['id'])
                product.quantity = product.quantity - item['quantity']
                product.save()
                #return para o pagamento mercado pago
            cart.clear()

        return redirect(reverse('home'))