# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.Proveedor'),
        ),
    ]
