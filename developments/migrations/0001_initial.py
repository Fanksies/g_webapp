# Generated by Django 2.0.13 on 2019-02-25 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Amenidad')),
                ('icon', models.CharField(max_length=128, verbose_name='Icono')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Amenidad',
                'verbose_name_plural': 'Amenidades',
            },
        ),
        migrations.CreateModel(
            name='BlueprintGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('name', models.CharField(max_length=256, verbose_name='Título')),
                ('description', models.CharField(max_length=256, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Galeria de planos',
                'verbose_name_plural': 'Galeria de planos',
            },
        ),
        migrations.CreateModel(
            name='Development',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nombre')),
                ('slug', models.SlugField(max_length=256, verbose_name='Slug')),
                ('address', models.CharField(max_length=256, verbose_name='Dirección')),
                ('description', models.CharField(max_length=256, verbose_name='Resumen')),
                ('neighborhood', models.CharField(max_length=256, verbose_name='Colonia')),
                ('slogan', models.CharField(max_length=256, verbose_name='Slogan')),
                ('status', models.CharField(choices=[('compra', 'Compra'), ('renta', 'Renta'), ('proximamente', 'Proximamente'), ('completado', 'Completado')], default='completado', max_length=32, verbose_name='Status')),
                ('about', models.TextField(max_length=256, verbose_name='Acerca del desarrollo')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagen principal')),
                ('video', models.FileField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Desarrollo',
                'verbose_name_plural': 'Desarrollos',
            },
        ),
        migrations.CreateModel(
            name='PictureGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('name', models.CharField(max_length=256, verbose_name='Título')),
                ('description', models.CharField(max_length=256, verbose_name='Descripción')),
                ('development', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developments.Development', verbose_name='Desarrollo')),
            ],
            options={
                'verbose_name': 'Galeria del desarrollo',
                'verbose_name_plural': 'Galeria de desarrollos',
            },
        ),
        migrations.AddField(
            model_name='blueprintgallery',
            name='development',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developments.Development', verbose_name='Desarrollo'),
        ),
        migrations.AddField(
            model_name='amenities',
            name='development',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developments.Development', verbose_name='Desarrollo'),
        ),
    ]
