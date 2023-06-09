from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tablon(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(verbose_name='fotoTablon', upload_to='famFeed', null=True)
    creador = models.ForeignKey(User, verbose_name='creador', on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(User, related_name='tablones', verbose_name='usuarios')

    class Meta:
        verbose_name = 'tablon'
        verbose_name_plural = 'tablones'