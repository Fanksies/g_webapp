# Generated by Django 2.0.13 on 2019-02-27 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developments', '0003_auto_20190227_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='development',
            name='category',
            field=models.ManyToManyField(to='developments.Type'),
        ),
        migrations.AlterField(
            model_name='development',
            name='status',
            field=models.ManyToManyField(to='developments.Status'),
        ),
    ]