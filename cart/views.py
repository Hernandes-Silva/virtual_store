from django.shortcuts import get_object_or_404, redirect, render
from rolepermissions.checkers import has_permission
from django.urls.base import reverse
from rolepermissions.roles import assign_role, get_user_roles
from django.views.decorators.http import require_POST
from cart.cart import Cart
from products.models import Product

# Create your views here.
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if product.quantity > 0:
        cart.add(product)
    return redirect(reverse('cart_detail'))
def cart_detail(request):
    cart = Cart(request)
    total_price = 0
    item_quantity = 0
    if cart:
        for item in cart:
            item_quantity += 1
            total_price += item['total_price']
    context = {'cart': cart, 'total_price':total_price, 'item_quantity': item_quantity}
    return render(request, 'cart_detail.html', context)
@require_POST
def cart_update(request):
    cart = Cart(request)
    product = get_object_or_404(Product, id = request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    cart.update(product, quantity)
    return redirect(reverse('cart_detail'))
@require_POST
def cart_remove(request):
    cart = Cart(request)
    product = get_object_or_404(Product, id = request.POST['id'])
    cart.remove(product)
    return redirect(reverse('cart_detail'))