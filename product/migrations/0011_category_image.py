# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_productimage_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='default/NO_IMAGE.png', upload_to='category_images'),
        ),
    ]
