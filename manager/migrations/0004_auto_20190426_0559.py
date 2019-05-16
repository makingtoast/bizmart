# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-04-26 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20190425_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdtl',
            name='product',
        ),
        migrations.AddField(
            model_name='orderdtl',
            name='product',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Product'),
        ),
    ]
