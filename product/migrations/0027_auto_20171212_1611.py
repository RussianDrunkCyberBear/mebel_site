# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20171212_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_descript',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.ProductStock', verbose_name='Акция'),
        ),
    ]
