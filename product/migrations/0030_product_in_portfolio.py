# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-21 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_auto_20171220_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_portfolio',
            field=models.BooleanField(default=False, verbose_name='Товар из портфолио (показывать в начале каталога)'),
        ),
    ]
