from django.db import models
from products.models import Product
# Create your models here.
class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
class Payment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    mercadopago_id = models.IntegerField()
    status = models.CharField(max_length=15)
    installments = models.IntegerField("Parcelas")
