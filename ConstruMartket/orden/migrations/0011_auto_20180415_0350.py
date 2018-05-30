# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-15 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orden', '0010_auto_20180415_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_orden',
            name='id_orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orden.Orden'),
        ),
        migrations.AlterField(
            model_name='detalle_orden',
            name='id_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Producto'),
        ),
        migrations.AlterField(
            model_name='detalle_pago',
            name='id_orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orden.Orden'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='id_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.Proveedor'),
        ),
    ]
