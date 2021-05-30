from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Department(models.Model):
    name = models.CharField(verbose_name=_('Department name'), max_length = 100)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(verbose_name=_('Category name'), max_length = 100)
    slug = models.SlugField(unique=True)
    department = models.ForeignKey(Department, related_name="categories", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name=_('Product name'), max_length = 100)
    price = models.FloatField(verbose_name=_('Product price'))
    quantity = models.PositiveIntegerField(verbose_name=_('Product stock'))
    image = models.ImageField(null=True, blank=True, upload_to="images/products/")
    information = models.TextField(verbose_name=_('Product information'))
    technical_information = models.TextField(verbose_name=_('technical Product information'))
    category = models.ForeignKey(Category,related_name="products", on_delete=models.CASCADE)
    brand = models.CharField(verbose_name=_('Product brand'), max_length=100)

    def __str__(self):
        return self.name