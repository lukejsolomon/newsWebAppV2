# Generated by Django 3.0.8 on 2020-12-15 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.URLField(blank=True, default=''),
        ),
    ]
