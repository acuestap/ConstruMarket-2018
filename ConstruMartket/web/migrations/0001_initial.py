# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 05:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(verbose_name='fecha compra')),
                ('valor', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Pago'),
        ),
    ]
