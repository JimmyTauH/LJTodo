# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0003_auto_20170130_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='calender',
            name='event_id',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
