# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cliente(models.Model):
    tipo_identificacion = models.CharField(max_length=20, default="Cedula")
    identificacion = models.CharField(max_length=50)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True)
    primer_apellido = models.CharField(max_length=50, blank=True)
    segundo_apellido = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.identificacion


