# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Orden, Detalle_orden, Detalle_pago
# Register your models here.
admin.site.register(Orden)#this line added
admin.site.register(Detalle_orden)#this line added
admin.site.register(Detalle_pago)#this line added