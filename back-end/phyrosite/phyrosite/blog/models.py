from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(unique=True, max_length=255)
    def __unicode__(self):
        return self.descripcion

class Tag(models.Model):
    descripcion = models.CharField(unique=True, max_length=255)
    def __unicode__(self):
        return self.descripcion

class Post(models.Model):
    publico = models.BooleanField(default=False)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    urlAmigable = models.CharField(unique=True, max_length=255)
    contenido = models.TextField()
    tags = models.ManyToManyField('Tag')
    categorias = models.ManyToManyField('Categoria')
    imgPrincipal = models.ImageField(upload_to='items/galerias', blank=True, null=True)
    imgPrincipalUrl = models.CharField(blank=True, null=True, max_length=255)
    imgDescription = models.CharField(blank=True, null=True, max_length=255)
    fecha = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.titulo
    