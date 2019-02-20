from django.db import models
from django.utils import timezone
import datetime

from administracion.models import Bodegas

# Create your models here.

class Item(models.Model):
    nombre = models.CharField(max_length=50)
    sku = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=100)
    costo = models.FloatField()
    peso = models.FloatField()
    ancho = models.FloatField()
    alto = models.FloatField()
    profundidad = models.FloatField()
    def __str__(self):
        return(self.nombre)
    
class Stock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    bodega = models.ForeignKey(Bodegas, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.cantidad)
