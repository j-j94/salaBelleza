# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_auto_20170613_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name_plural': 'Productos'},
        ),
        migrations.AddField(
            model_name='factura',
            name='productos',
            field=models.ManyToManyField(through='facturacion.DetFactura', to='facturacion.Producto'),
        ),
    ]
