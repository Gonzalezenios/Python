from django.db import models

# Create your models here.
class Comanda(models.Model):
    orden = models.CharField(max_length = 120)