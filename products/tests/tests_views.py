from django.test import TestCase, Cliente
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Department, Product, Category

class TestView(TestCase):
    def setUp(self):
        print('# -- Setup Function --')
        password = 'admin'
        user = User.objects.create_superuser('admin', 'admin@gmail.com', password)
        self.client.login(username=user.username, password = password)
        print('# -- End Setup Function\n')
    #ListDepartmentView

    def test_GET_list_department(self):
        #falta verificar se estar logado
        print('# Testing -- GET list department -- view')
        
        department  = Department.objects.create(name= "Informática")
        response = self.client.get(reverse('department_list'))

        print("--- init Testing request")
        self.assertEquals(response.status_code, 200)
        print('--- end Testing request\n')

        print("--- init Testing template used")
        self.assertTemplateUsed(response, "department_list.html")
        print('-- end Testing template used\n')

        print("--- init Testing len context")
        self.assertEquals(len(response.context['departments']), 1)
        print("--- end Testing len context")

        print("--- init Testing context")
        self.assertEquals(response.context['departments'][0].name, 'Informática')
        print("--- end Testing context")

        print('# End Testing -- GET list department -- view\n')

    #CreateDepartmentView

    def test_GET_create_department(self):
        print('# Testing -- GET create department -- view')

        response = self.client.get('department_create')

        print("--- init Testing request")
        self.assertEquals(response.status_code, 200)
        print('--- end Testing request\n')

        print("--- init Testing template used")
        self.assertTemplateUsed(response, 'department_create.html')
        print('--- end Testing template used\n')

        print('# End Testing -- GET create department -- view\n')

    def test_POST_create_department(self):
        print('# Testing -- POST create department -- view')
        url = reverse('department_create')
        response = self.client.post(url, { 
            'name' : 'Informática'
        })

        print("--- init Testing request")
        self.assertEquals(response.status_code, 302)
        print('--- end Testing request\n')

        print("--- init Testing success POST")
        self.assertEquals(Department.objects.all().first().name, "Informática")
        print('--- end Testing success POST\n')
        print('# End Testing -- POST create department -- view\n')


    #listCategoryView
    def test_GET_list_category(self):
        print('# Testing -- GET list category -- view')

        response = self.client.get(reverse('category_list'))

        print("--- init Testing request")
        self.assertEquals(response.status_code, 200)
        print('--- end Testing request\n')

        print("--- init Testing template used")
        self.assertTemplateUsed(response, 'category_list.html')
        print("--- end Testing template used\n")

        print("--- init Testing len context")
        self.assertEquals(len(response.context['categories']), 1)
        print("--- end Testing len context")

        print("--- init Testing context")
        self.assertEquals(response.context['categories'][0].name, 'computadores')
        print("--- end Testing context")

        print('# end Testing -- GET list category -- view\n')

    #CreateCategoryView

    def test_GET_create_category(self):
        print('# Testing -- GET create category -- view')
        department  = Department.objects.create(name= "Informática")
        category = Category.objects.create(name='computadores', department= department)
        response = self.client.get(reverse('category_list'))
        
        print("--- init Testing request")
        self.assertEquals(response.status_code, 200)
        print('--- end Testing request\n')

        print("--- init Testing template used")
        self.assertTemplateUsed(response, 'category_create.html')
        print("--- end Testing template used\n")

        print('# end Testing -- GET create category -- view\n')

    def test_POST_create_category(self):
        print('# Testing -- POST list category -- view')
        department  = Department.objects.create(name= "Informática")
        response = self.client.post(reverse('category_create'), {
            'name' : "computadores",
            'department': department
        })
        print("--- init Testing request")
        self.assertEquals(response.status_code, 302)
        print('--- end Testing request\n')

        print("--- init Testing success POST")
        self.assertEquals(Category.objects.all().first().name, "computadores")
        print('--- end Testing success POST\n')

        print('# end Testing -- POST list category -- view\n')
        





