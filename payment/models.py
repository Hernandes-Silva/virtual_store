from django.db import models
from django.db.models.fields import CharField
from products.models import Product
from order.models import Order
from django.contrib.auth.models import User
# Create your models here.

class Payment(models.Model):
    class Meta:
        ordering = ['-created']
    user = models.ForeignKey(User, related_name="payments", on_delete=models.CASCADE)
    order = models.ForeignKey(Order,related_name="order", on_delete=models.CASCADE)
    mercadopago_id = models.IntegerField()
    status = models.CharField(max_length=150)
    installments = models.IntegerField("Parcelas")
    status_detail = CharField(max_length=250)
    payment_method = CharField(max_length=250)
    payment_type = CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
