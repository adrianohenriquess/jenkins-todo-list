# Generated by Django 2.1.7 on 2023-01-09 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230109_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 1, 9, 17, 15, 37, 168702)),
        ),
    ]
