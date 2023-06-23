from django.db import models

# Create your models here.

#creando tabla
class Book(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()