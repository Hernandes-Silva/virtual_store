
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
        department  = Department.objects.create(name= "Informática")
        category = Category.objects.create(name="computadores", department = department)
        self.product = Product.objects.create(name="Pc gamer", price = 10, stock= 50, information = "I5 com 10gb de ram",
        technical_information = "Super veloz", category = category, brand="Asus")
        print('# -- End Setup Function\n')

    def test_add_product_in_cart(self):
        print('# -- Testing add product in cart -- view ')
        self.client.get(reverse('cart_add', args=[self.product.pk]))
        cart = self.client.session['cart'][str(self.product.pk)]
        self.assertEquals(cart['name'], "Pc gamer")
        print('# -- end Testing add product in cart -- view \n')

    def test_GET_detail_cart(self):
        print('# -- Testing Get cart deatil -- view ')
        response = self.client.get(reverse('cart_detail'))
        print(" --- init testing request ---")
        self.assertEquals(response.status_code, 200)
        print(" --- end testing request ---\n")

        print(" --- init template used ---")
        self.assertTemplateUsed(response, 'cart_detail.html')
        print(" --- end template used ---\n")

        print(" --- init testing session cart")

        print('# -- end Testing Get cart deatil -- view \n')

