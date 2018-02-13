# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20171115_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_image', to='product.ProductImage', verbose_name='Основное изображение'),
        ),
    ]
