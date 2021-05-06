from django.test import TestCase
from django.url import resolve, reverse
from products import views
# Create your tests here.
class TestUrl(TesteCase):
    def test_list_department_url_resolve(self):
        print("# Testing -- list department -- url resolve")

        url = reverse('department_url')
        self.assertEquals(resolve(url).func.view_class, views.ListDepartmentView)

        print("# End Testing -- list department -- url resolve\n")

    def test_create_department_url_resolve(self):
        print("# Testing -- create department -- url resolve")

        url = reverse('department_create')
        self.assertEquals(resolve(url).func.views_class, views.CreateDepartmentView)

        print("# End Testing -- create department -- url resolve\n")

    def test_list_category_url_resolve(self):
        print("# Testing -- list category -- url resolve")

        url = reverse('category_list')
        self.assertEquals(resolve(url).func.view_class, views.ListCategoryView)

        print("# End Testing -- list category -- url resolve\n")

    def test_create_category_url_resolve(self):
        print("# Testing -- list category -- url resolve")

        url = reverse('category_create')
        self.assertEquals(resolver(url).func.view_class, view.CreateCategoryView)