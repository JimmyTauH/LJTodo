# Generated by Django 4.2.13 on 2024-06-09 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0010_auto_20170319_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 18, 4, 31, 29389, tzinfo=datetime.timezone.utc)),
        ),
    ]
