# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 05:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_product_main_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='is_main',
        ),
    ]