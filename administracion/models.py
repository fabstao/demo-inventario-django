from django.db import models

# Create your models here.

class Bodegas(models.Model):
    nombre = models.CharField(max_length=25)
    calle = models.CharField(max_length=30)
    exterior = models.CharField(max_length=10)
    interior = models.CharField(max_length=15)
    fraccionamiento = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    codigo_postal = models.CharField(max_length=6)
    entidad = models.CharField(max_length=25)
    pais = models.CharField(max_length=25)
    telefono = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "Bodegas"
    def __str__(self):
        return(self.nombre)


