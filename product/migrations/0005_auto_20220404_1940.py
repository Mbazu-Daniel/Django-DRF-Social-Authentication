# Generated by Django 3.2.9 on 2022-04-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20220404_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='facebook_profile',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='github_profile',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='hashnode_profile',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='instagram_profile',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='linkedin_profile',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='medium_profile',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='youtube_profile',
            field=models.CharField(max_length=200),
        ),
    ]