from django.contrib.sessions import middleware
from django.urls.base import reverse
from products.models import Category, Department, Product
from cart.cart import Cart
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest
class TestClassCart(TestCase):
    def setUp(self):
        print('# -- Setup Function --')
        self.http_request = HttpRequest()
        middleware = SessionMiddleware(None)
        middleware.process_request(self.http_request)
        self.session = self.http_request.session

        department  = Department.objects.create(name= "Informática")
        category = Category.objects.create(name="computadores", department = department)
        self.product = Product.objects.create(name="Pc gamer", price = 10, stock= 50, information = "I5 com 10gb de ram",
        technical_information = "Super veloz", category = category, brand="Asus")
        print('# -- End Setup Function\n')

    def test_create_empty_cart(self):
        print('# --- Testing create empty cart -- class')
        self.assertEqual(self.session.get('cart'), None)
        Cart(self.http_request)
        self.assertEqual(self.session.get('cart'), {})
        print('# --- end Testing create empty cart -- class\n')
    def test_get_non_empty_cart(self):
        print('# --- Testing get non empty cart -- class')
        self.session['cart'] = {"1": {}}
        Cart(self.http_request)
        self.assertEqual(self.session['cart'], {"1": {}})
        print('# --- endTesting get non empty cart -- class\n')
    def test_add_product_to_empty_cart(self):
        print('# --- Testing add product to empty cart  -- class')
        cart = Cart(self.http_request)
        cart.add(self.product)
        session_cart = self.session['cart'][str(self.product.id)]
        self.assertEqual(session_cart['name'], "Pc gamer")
        print('# --- end Testing add product to empty cart  -- class\n')
        
    
