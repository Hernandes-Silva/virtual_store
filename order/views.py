from django.http.response import HttpResponseRedirect
from products.models import Product
from order.forms import OrderForm
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from order.models import Order, Item
from cart.cart import Cart
from order.forms import OrderForm





class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    def form_valid(self, form):
        if self.request.session['cart']:
            order = form.save()
            for item in self.request.session['cart']:
                product = Product.objects.get(pk=item)
                quantity = self.request.session['cart'][item]['quantity']
                Item.objects.create(
                    order=order,
                    product=product,
                    price=self.request.session['cart'][item]['price'],
                    quantity=quantity
                )
                product.quantity = product.quantity - quantity
                product.save()
            del self.request.session['cart']
            self.request.session.modified = True
            return HttpResponseRedirect(reverse_lazy('payment', args=[order.id]))
        return HttpResponseRedirect(reverse('home'))
