# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerfinder', '0003_auto_20160816_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='phone_number',
            field=models.CharField(default='(541) 563-6181', max_length=15),
        ),
    ]
