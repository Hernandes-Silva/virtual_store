
from django.urls.base import reverse
from products.models import Category, Department, Product
from django.test import TestCase, Client
from django.contrib.auth.models import User
# Create your tests here.
class TestCart(TestCase):
    def setUp(self):
        print('# -- Setup Function --')
        password = 'admin'
        user = User.objects.create_superuser('admin', 'admin@gmail.com', password)
        self.client.login(username=user.username, password = password)
        department  = Department.objects.create(name= "Informática", slug='informatica')
        category = Category.objects.create(name="computadores", department = department, slug='computadores')
        self.product = Product.objects.create(name="Pc gamer", price = 10, quantity= 50, information = "I5 com 10gb de ram",
        category = category, brand="Asus")
        print('# -- End Setup Function\n')

    def test_add_product_in_cart(self):
        print('# -- Testing add product in cart -- view ')
        self.client.get(reverse('cart_add', args=[self.product.pk]))
        cart = self.client.session['cart'][str(self.product.pk)]
        self.assertEquals(cart['name'], "Pc gamer")
        print('# -- end Testing add product in cart -- view \n')

    def test_GET_cart_detail(self):
        print('# -- Testing Get cart detail -- view ')
        response = self.client.get(reverse('cart_detail'))
        print(" --- init testing request ---")
        self.assertEquals(response.status_code, 200)
        print(" --- end testing request ---\n")
        print(" --- init template used ---")
        self.assertTemplateUsed(response, 'cart_detail.html')
        print(" --- end template used ---\n")
        print('# -- end Testing Get cart deatil -- view \n')

    def test_POST_cart_remove(self):
        print('# -- Testing POST cart remove -- view ')
        self.client.get(reverse('cart_add', args=[self.product.pk]))
        self.assertIn(str(self.product.pk), self.client.session['cart'])
        response = self.client.post(reverse("cart_remove"), {"id":self.product.id})
        print(" --- init testing request ---")
        self.assertEquals(response.status_code, 302)
        print(" --- end testing request ---\n")
        print(" --- init testing success post ---") 
        self.assertNotIn(str(self.product.pk), self.client.session['cart'])
        print(" --- end init testing success post ---\n") 
        print('# -- end Testing POST cart remove -- view \n')

    def test_POST_cart_update(self):
        print('# -- Testing POST cart update -- view ')
        self.client.get(reverse('cart_add', args=[self.product.pk]))
        self.assertIn(str(self.product.pk), self.client.session['cart'])
        response = self.client.post(reverse("cart_update"), {"product_id":self.product.id, "quantity": 5})
        print(" --- init testing request ---")
        self.assertEquals(response.status_code, 302)
        print(" --- end testing request ---\n")
        print(" --- init testing success post ---") 
        cart = self.client.session['cart'][str(self.product.pk)]
        self.assertEqual(cart['quantity'], 5)
        print(" --- end init testing success post ---\n")
        print('# -- end Testing POST cart update -- view \n')


