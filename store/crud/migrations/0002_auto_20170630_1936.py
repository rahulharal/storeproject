# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-30 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
