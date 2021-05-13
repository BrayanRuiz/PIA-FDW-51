from django.db import models
from .models import *

# Create your models here.
class Estanteria(models.Model):
    nombre = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    precio = models.FloatField()
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    dimensiones_del_producto = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
        
class Lockers(models.Model):
    nombre = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    precio = models.FloatField()
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    dimensiones_del_producto = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre