# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from proveedor.models import Proveedor

# Create your models here.

class Producto(models.Model):
    id_proveedor = models.ForeignKey(Proveedor)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=50, blank=True)
    valor_unitario = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre