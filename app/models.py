from django.db import models
from .models import *

# Create your models here.
class Estanteria(models.Model):
    fabricante = models.CharField(max_length=50)
    precio = models.IntegerField()
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    dimensiones_del_producto = models.CharField(max_length=50)
    id_est = models.IntegerField()
    def __str__(self):
        return self.fabricante
        
class Lockers(models.Model):
    fabricante = models.CharField(max_length=50)
    precio = models.FloatField()
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    dimensiones_del_producto = models.CharField(max_length=50)
    id_lock = models.IntegerField()
    def __str__(self):
        return self.fabricante