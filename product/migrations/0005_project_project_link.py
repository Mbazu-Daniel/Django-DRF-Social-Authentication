# Generated by Django 3.2.9 on 2022-04-16 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_project_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
