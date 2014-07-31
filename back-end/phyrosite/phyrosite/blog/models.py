from django.db import models

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(unique=True, max_length=255)
    def __unicode__(self):
        return self.descripcion

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    lugar = models.TextField()
    inicia = models.DateTimeField()
    termina = models.DateTimeField()
    

    def __unicode__(self):
        pass
    