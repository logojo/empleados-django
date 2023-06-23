from django.contrib import admin
from .models import Empleado, Habilidad
# Register your models here.
admin.site.register(Habilidad)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name'
    )

    #el obj trae cada uno los registros que itera el administrador
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name
    # 

    search_fields = ('first_name','last_name',)
    list_filter= ('departamento','job','Habilidades',)
    filter_horizontal = ('Habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)