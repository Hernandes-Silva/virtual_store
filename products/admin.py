from products.models import Category, Department, Product
from django.contrib import admin
from products.models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(TechnicalInformation)
admin.site.register(Department)
admin.site.register(Category)