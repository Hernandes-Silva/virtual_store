from django.db import models
from products.models import Product
from django.core.validators import MinValueValidator
from localflavor.br.models import BRCPFField, BRPostalCodeField, BRStateField
from model_utils.models import TimeStampedModel


# Create your models here.
class Order(TimeStampedModel):
    cpf = BRCPFField("cpf")
    name = models.CharField("Nome Completo", max_length=250)
    email = models.EmailField()
    postal_code = BRPostalCodeField("CEP")
    state = BRStateField("Estado")

class Item(models.Model):
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1),])
