# Generated by Django 3.2.9 on 2022-04-16 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
