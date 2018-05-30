# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from cliente.models import Cliente
from proveedor.models import Proveedor
from producto.models import Producto
# Create your models here.

class Orden(models.Model):
    id_cliente = models.ForeignKey(Cliente)
    id_proveedor = models.ForeignKey(Proveedor)
    fecha_orden = models.DateTimeField('fecha compra')

    def __int__(self):
        return self.pk



class Detalle_orden(models.Model):
    id_orden = models.ForeignKey(Orden)
    id_producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField(default=0)
    valor = models.IntegerField(default=0)

    def __int__(self):
        return self.pk


class Detalle_pago(models.Model):
    id_orden = models.ForeignKey(Orden)
    valor_total = models.IntegerField(default=0)
    fecha_pago = models.DateTimeField('fecha pago')
    medio_pago = models.CharField(max_length=100, blank=True)
    estado = models.BooleanField(default=1)

    def __int__(self):
        return self.pk