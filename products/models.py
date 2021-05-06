from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Department(models.Model):
    name = models.CharField(verbose_name=_('Department name'), max_length = 100)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(verbose_name=_('Category name'), max_length = 100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name=_('Product name'), max_length = 100)
    price = models.FloatField(verbose_name=_('Product price'))
    stock = models.PositiveIntegerField(verbose_name=_('Product stock'))
    information = models.TextField(verbose_name=_('Product information'))
    technical_information = models.TextField(verbose_name=_('technical Product information'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(verbose_name=_('Product brand'), max_length=100)

    def __str__(self):
        return self.name