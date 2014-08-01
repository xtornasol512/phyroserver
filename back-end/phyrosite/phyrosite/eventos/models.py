from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    lugar = models.TextField()
    inicia = models.DateTimeField()
    termina = models.DateTimeField()