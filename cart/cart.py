from products.models import Product
from decimal import Decimal
class Cart:
    def __init__(self, request):
        if request.session.get('cart') is None:
            request.session['cart'] = {}
        self.cart = request.session['cart']
        self.session = request.session
    def __iter__(self):
        products = Product.objects.filter(id__in=self.cart)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['totakl_price'] = item['price'] * item['quantity']
            yield item
    def add(self, product):
        self.cart[str(product.id)] = {
            "name": product.name,
            "quantity" : 1,
            "price" : str(product.price)
        }
        self.session.modified = True
    def remove(self, product):
        del self.cart[str(product.id)]
        self.session.modified = True


