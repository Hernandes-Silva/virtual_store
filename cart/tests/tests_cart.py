from django.test import TestCase, Client
from django.contrib.auth.models import User
# Create your tests here.
class TestCart(TestCase):
    def setUp(self):
        print('# -- Setup Function --')
        password = 'admin'
        user = User.objects.create_superuser('admin', 'admin@gmail.com', password)
        self.client.login(username=user.username, password = password)
        session = self.client.session
        print('# -- End Setup Function\n')
