# Generated by Django 3.0.8 on 2020-12-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20201201_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='contact',
        ),
        migrations.AddField(
            model_name='article',
            name='byProfile',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='profile',
            field=models.CharField(blank=True, default='', max_length=3),
        ),
    ]
