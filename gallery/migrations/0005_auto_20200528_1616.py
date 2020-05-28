# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-28 16:16
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20200526_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=90, size=[800, 800], upload_to='images'),
        ),
    ]
