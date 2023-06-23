from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('nombre', max_length=50)
    short_name = models.CharField('nombre_corto', max_length=20, blank=True, null=True, unique=True)
    status = models.BooleanField('status', default=True)
    
    #Esta clase permite definir los nombres con los que aparecera la tabla en el administrador de django
    class Meta:
        verbose_name = 'Deparment'
        verbose_name_plural =  'Áreas de la empresa'
        ordering = ['-name'] #el guión indica que se ordenara en orden inverso
        unique_together =  ('name', 'short_name') #evita que se registren nombres duplicados o convinaciones de nombre de campo de departamento

    def __str__( self ):
        return str(self.id) + '-' + self.name + '-' + self.short_name