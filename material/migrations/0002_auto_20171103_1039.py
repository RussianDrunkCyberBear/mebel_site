# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='material_image',
            field=models.ImageField(default='images/NO_IMAGE.png', upload_to='material_images'),
        ),
        migrations.AlterField(
            model_name='materialcategory',
            name='url_name',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]
