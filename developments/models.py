from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Development(models.Model):

    class Meta:
        verbose_name = 'Desarrollo'
        verbose_name_plural = 'Desarrollos'

    def __str__(self):
        return self.name


    name = models.CharField('Nombre', max_length=256)
    slug = models.SlugField('Slug', max_length=256)

    address = models.CharField('Dirección', max_length=256)
    description = models.TextField('Resumen', max_length=1056)
    neighborhood = models.CharField('Colonia', max_length=256)
    slogan = models.CharField('Slogan', max_length=256)
    status = models.ManyToManyField('developments.Status')
    category = models.ManyToManyField('developments.Type')
    about = models.TextField('Acerca del desarrollo', max_length=1056)
    is_featured = models.BooleanField('Aparece en el home?', default=False)

    image = models.ImageField('Imagen principal')
    logo = models.ImageField('Logo del desarrollo', null=True, blank=True)
    video = models.CharField('url del video subido a un CDN', blank=True, max_length=256)
    website = models.URLField(blank=True)


class PictureGallery(models.Model):

    class Meta:
        verbose_name = 'Galeria del desarrollo'
        verbose_name_plural = 'Galeria de desarrollos'

    development = models.ForeignKey(
        Development, verbose_name='Desarrollo', on_delete=models.CASCADE)
    image = models.ImageField('Imagen')
    name = models.CharField('Título', max_length=256)
    description = models.CharField('Descripción', max_length=256)


class BlueprintGallery(models.Model):

    class Meta:
        verbose_name = 'Galeria de planos'
        verbose_name_plural = 'Galeria de planos'

    development = models.ForeignKey(
        Development, verbose_name='Desarrollo', on_delete=models.CASCADE)
    image = models.ImageField('Imagen')
    name = models.CharField('Título', max_length=256)
    description = models.CharField('Descripción', max_length=256)


class Amenities(models.Model):

    class Meta:
        verbose_name = 'Amenidad'
        verbose_name_plural = 'Amenidades'

    development = models.ForeignKey(
        Development, verbose_name='Desarrollo', on_delete=models.CASCADE)
    name = models.CharField('Amenidad', max_length=128)
    icon = models.CharField('Icono', max_length=128)
    description = models.TextField('Descripción')


class Status(models.Model):

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    name = models.CharField('Status', max_length=128)

    def __str__(self):
        return self.name


class Type(models.Model):

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['name']

    name = models.CharField('Type', max_length=128)

    def __str__(self):
        return self.name
