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
        self.session_name = "cart"
        department  = Department.objects.create(name= "Informática", slug='informatica')
        category = Category.objects.create(name="computadores", department = department, slug='computadores')
        self.product = Product.objects.create(name="Pc gamer", price = 10, quantity= 50, information = "I5 com 10gb de ram",
        category = category, brand="Asus")
        print('# -- End Setup Function\n')
    def test_create_empty_cart(self):
        print('# --- Testing create empty cart -- class')
        self.assertEqual(self.session.get(self.session_name), None)
        Cart(self.http_request)
        self.assertEqual(self.session.get(self.session_name), {})
        print('# --- end Testing create empty cart -- class\n')
    def test_get_non_empty_cart(self):
        print('# --- Testing get non empty cart -- class')
        self.session[self.session_name] = {"1": {}}
        Cart(self.http_request)
        self.assertEqual(self.session[self.session_name], {"1": {}})
        print('# --- endTesting get non empty cart -- class\n')
    def test_add_product_to_empty_cart(self):
        print('# --- Testing add product to empty cart  -- class')
        cart = Cart(self.http_request)
        cart.add(self.product)
        session_cart = self.session[self.session_name][str(self.product.id)]
        self.assertEqual(session_cart['name'], "Pc gamer")
        print('# --- end Testing add product to empty cart  -- class\n')
    def test_remove_product_cart(self):
        print('# --- Testing remove product cart  -- class')
        cart = Cart(self.http_request)
        cart.add(self.product)
        session_cart = self.session[self.session_name][str(self.product.id)]
        self.assertEqual(session_cart['name'], "Pc gamer")
        cart.remove(self.product)
        self.assertNotIn(str(self.product.id), self.session[self.session_name])
        print('# --- end Testing remove product cart  -- class\n')
    def test_update_product_cart(self):
        print('# --- Testing update product cart  -- class')
        cart = Cart(self.http_request)
        cart.add(self.product)
        session_cart = self.session[self.session_name][str(self.product.id)]
        self.assertEqual(session_cart['quantity'], 1)
        cart.update(self.product, 3)
        session_cart = self.session[self.session_name][str(self.product.id)]
        self.assertEqual(session_cart['quantity'], 3)
        print('# --- end Testing update product cart  -- class\n')


        
    
