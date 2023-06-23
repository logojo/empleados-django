from django.db import models

#importando modelo para relacionar
from  applications.departamento.models import Departamento

#Utilizando aplicacion de terceros checkditor
from ckeditor.fields import RichTextField

class Habilidad(models.Model):
    habilidad = models.CharField('habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidades'
        verbose_name_plural =  'Habilidad de empleado'

    def __str__( self ):
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):

    JOB_CHOISES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )

    first_name = models.CharField('first_name', max_length=50)
    last_name = models.CharField('last_name', max_length=50)
    full_name = models.CharField('full_name', max_length=120, blank=True)
    job = models.CharField('job', max_length=50, choices=JOB_CHOISES)  #tipo enum
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='empleado', blank=True, null=True)
    Habilidades = models.ManyToManyField(Habilidad)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural =  'empleados de la empresa'
        ordering = ['-first_name'] #el guión indica que se ordenara en orden inverso

    def __str__( self ):
        return str(self.id) + '-' + self.first_name + ' ' + self.last_name