from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse
from cart.cart import Cart
from products.models import Product

# Create your views here.
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect(reverse('cart_detail'))
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})
#@Required_POST
def cart_remove(request):
    cart = Cart(request)
    product = get_object_or_404(Product, id = request.POST['id'])
    cart.remove(product)
    return redirect(reverse('cart_detail'))