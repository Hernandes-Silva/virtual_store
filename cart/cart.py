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
            #item['total_price'] = item['price'] * item['quantity']
            yield item
    def add(self, product):
        self.cart[str(product.id)] = {
            "name": product.name,
            "quantity" : 1,
            "price" : str(product.price)
        }
        self.session.modified = True
    def update(self, product, quantity=1):
        self.cart[str(product.id)] = {
            "name": product.name,
            "quantity" : quantity,
            "price" : str(product.price)
        }
        self.session.modified = True
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True


