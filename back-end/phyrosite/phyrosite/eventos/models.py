from django.db import models
from phyrosite.blog.models import Post

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    lugar = models.TextField()
    inicia = models.DateTimeField()
    termina = models.DateTimeField()
    posts = models.ManyToManyField('Post', blank=True, null=True)
    def __unicode__(self):
    	return self.titulo