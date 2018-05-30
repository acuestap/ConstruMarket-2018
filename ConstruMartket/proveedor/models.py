# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Proveedor(models.Model):
    razon_social = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    ciudad = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.razon_social

