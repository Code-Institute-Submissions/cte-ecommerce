# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-26 15:45
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200526_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, size=[1000, 1000], upload_to='images'),
        ),
    ]
