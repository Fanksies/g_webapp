# Generated by Django 2.0.13 on 2019-04-09 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developments', '0006_development_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='development',
            name='video',
            field=models.CharField(blank=True, max_length=256, verbose_name='url del video subido a un CDN'),
        ),
    ]