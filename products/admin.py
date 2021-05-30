from products.models import Category, Department, Product
from django.contrib import admin
from products.models import Product, Department, Category
# Register your models here.
admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Category)