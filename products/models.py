from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Department(models.Model):
    name = models.CharField(verbose_name=_('Department name'), max_length = 100)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(verbose_name=_('Category name'), max_length = 100)
    slug = models.SlugField(unique=True)
    department = models.ForeignKey(Department, related_name="categories", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name=_('Product name'), max_length = 250)
    price = models.FloatField(verbose_name=_('Product price'))
    quantity = models.PositiveIntegerField(verbose_name=_('Product quantity'))
    image = models.ImageField(null=True, blank=True, upload_to="images/products/")
    information = models.TextField(verbose_name=_('Product information'))
    category = models.ForeignKey(Category,related_name="products", on_delete=models.CASCADE)
    brand = models.CharField(verbose_name=_('Product brand'), max_length=100)

    def __str__(self):
        return self.name
class TechnicalInformation(models.Model):
    product = models.ForeignKey(Product, related_name="technical_informations", on_delete=models.CASCADE)
    information_tech = CharField(max_length=100)
    descricion = CharField(max_length=100)