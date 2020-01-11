from django.db import models

# Create your models here.
class Comanda(models.Model):
    orden = models.CharField(max_length = 120)
    usuario = models.CharField(max_length= 120)
    ubicacion= models.CharField(max_length= 120)