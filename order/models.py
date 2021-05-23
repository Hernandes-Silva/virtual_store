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
    phone = models.CharField("Telefone", max_length=100)
    postal_code = BRPostalCodeField("CEP")
    state = BRStateField("Estado")
    city = models.CharField("Cidade", max_length=100)
    district = models.CharField("Bairro", max_length=150)
    street = models.CharField("Rua", max_length=250)
    complement = models.CharField("Complemento", max_length=250, blank=True)
    number = models.CharField("Número", max_length=100)
    paid = models.BooleanField("Pago",default=False)
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Pedido {self.id}"

class Item(models.Model):
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1),])
