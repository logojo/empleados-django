#En este archivo se personalizan los formularios creados automaticamente
from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('__all__')
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Titulo del libro',
                    'class': 'form-field'
                }
            ),
            'cantidad': forms.NumberInput(
                  attrs={
                    'placeholder': 'Existencia'
                }
            )
        }

    #la funcion debe ir al nivel del class Meta, cuidar siempre la identación
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        #validando que cantidad sea mayor a 10
        if cantidad < 10:
            raise forms.ValidationError('La cantidad no debe ser menor a 10')
        
        return cantidad
