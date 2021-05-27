from django.db import models
from django.db.models.fields import CharField
from products.models import Product
from order.models import Order
# Create your models here.

class Payment(models.Model):
    order = models.ForeignKey(Order,related_name="order", on_delete=models.CASCADE)
    mercadopago_id = models.IntegerField()
    status = models.CharField(max_length=150)
    installments = models.IntegerField("Parcelas")
    status_detail = CharField(max_length=250)
    payment_method = CharField(max_length=250)
    payment_type = CharField(max_length=250)
