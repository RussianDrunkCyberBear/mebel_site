# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0003_auto_20171103_1040'),
        ('product', '0014_remove_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available_materials',
        ),
        migrations.AddField(
            model_name='product',
            name='materials_deck',
            field=models.ManyToManyField(blank=True, related_name='mat_deck', to='material.Material', verbose_name='Доступные материалы столешницы'),
        ),
        migrations.AddField(
            model_name='product',
            name='materials_face',
            field=models.ManyToManyField(blank=True, related_name='mat_face', to='material.Material', verbose_name='Доступные материалы фасада'),
        ),
        migrations.AddField(
            model_name='product',
            name='materials_others',
            field=models.ManyToManyField(blank=True, related_name='mat_others', to='material.Material', verbose_name='Доступные материалы другие'),
        ),
        migrations.AddField(
            model_name='product',
            name='materials_text',
            field=models.TextField(blank=True, verbose_name='Доступные материалы текстом (если нужно)'),
        ),
    ]
