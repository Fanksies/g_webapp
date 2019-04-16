# Generated by Django 2.0.13 on 2019-02-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developments', '0002_auto_20190225_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='development',
            name='category',
            field=models.ManyToManyField(blank=True, to='developments.Type'),
        ),
        migrations.AlterField(
            model_name='development',
            name='status',
            field=models.ManyToManyField(blank=True, to='developments.Status'),
        ),
    ]
