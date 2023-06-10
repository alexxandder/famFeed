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

class Recuerdo(models.Model):
    titulo = models.CharField(max_length=30)
    imagenRecuerdo = models.ImageField(verbose_name='imagenRecuerdo', upload_to='famFeedRecuerdos', null=True)
    texto = models.CharField(max_length=1000)
    autor = models.ForeignKey(User, verbose_name='autor', on_delete=models.CASCADE)
    tablon = models.ForeignKey(Tablon, related_name='recuerdos',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'recuerdo'
        verbose_name_plural = 'recuerdos'

class Comentario(models.Model):
    cuerpo = models.CharField(max_length=50)
    autor = models.ForeignKey(User, verbose_name='autor', on_delete=models.CASCADE)
    recuerdo = models.ForeignKey(Recuerdo, related_name='comentarios',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentario'