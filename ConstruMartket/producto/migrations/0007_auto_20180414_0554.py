# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-14 05:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_auto_20180414_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.Proveedor'),
        ),
    ]
