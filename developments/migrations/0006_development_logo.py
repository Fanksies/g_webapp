# Generated by Django 2.0.13 on 2019-03-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developments', '0005_auto_20190227_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='development',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Logo del desarrollo'),
        ),
    ]
