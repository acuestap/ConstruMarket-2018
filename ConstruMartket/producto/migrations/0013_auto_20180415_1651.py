# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-15 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0012_auto_20180415_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.Proveedor'),
        ),
    ]
