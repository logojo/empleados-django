from django import forms

from .models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'full_name',
            'job',
            'departamento',
            'image',
            'Habilidades',
            'hoja_vida',
        )
        widgets = {
            'Habilidades' : forms.CheckboxSelectMultiple()
        }
