# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-02 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_format', '0002_default_formats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='format',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Format title'),
        ),
    ]