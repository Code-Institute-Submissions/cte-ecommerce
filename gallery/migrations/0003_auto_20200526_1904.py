# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-26 19:04
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20200526_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=90, size=[1000, 1000], upload_to='images'),
        ),
    ]
