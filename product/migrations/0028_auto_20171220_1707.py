# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_auto_20171212_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='on_main_page',
            field=models.BooleanField(default=False, verbose_name='Показывать на главной'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(null=True, upload_to=product.models.prod_mainimage_upload_path),
        ),
    ]
