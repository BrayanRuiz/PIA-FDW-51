from django.db import models
from .models import *

# Create your models here.
class Estanteria(models.Model):
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField()
    def __str__(self):
        return self.descripcion
        
class Lockers(models.Model):
    descripcion = models.CharField(max_length=60)
    def __str__(self):
        return self.nombre