from django.db import models

# Create your models here.
class Card(models.Model):
    link = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/home/")
    descricion = models.CharField(max_length=250)
    price = models.FloatField()
