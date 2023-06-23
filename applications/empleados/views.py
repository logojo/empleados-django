
from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Empleado
from .forms import EmpleadoForm

class ListEmployees(ListView):
    #estos son Attributes
    template_name = 'empleados/index.html'
    #model = Empleado
    context_object_name = 'employees'
    #si no mando un context_object_name puedo acceder a los datos del modelo a de una variable generada por default llamada object_list

    #paginacion
    paginate_by = 5
    ordering = 'first_name'

    def get_queryset(self):  #funcion que realiza la busqueda de empleados por el campo fullname
        kword = self.request.GET.get('kword','')
        employees = Empleado.objects.filter(
            full_name__icontains = kword #el icontains busca rl texto excrito en el input dentro del fullname
        )
        return employees

class ListByArea(ListView):
    template_name = 'empleados/list_by_area.html'
    #Realizar busqueda de registros aplicando filtros

    def get_queryset(self):
        employees = Empleado.objects.filter(
            departamento__short_name = self.kwargs['short_name']
        )
        return employees

#Busqueda desde formulario
class ListByKword(ListView):
    template_name = 'empleados/by_kword.html'
    context_object_name = 'employees'

    def get_queryset(self):
        kword = self.request.GET.get('kword','')
        employees = Empleado.objects.filter(
            first_name = kword
        )
        return employees
    
class ListHabilidades(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        #recuperando datos una relacion mucho a muchos en este casa de la tabla habilidad nota el foreingkey es Habilidades
        print(empleado.Habilidades.all())
        return empleado.Habilidades.all()
    

#Esto es como la función "show" en laravel, recupera la información de un registro con un id dado
class EmpleadoDetailView(DetailView):
    template_name = "empleados/show.html"
    model = Empleado
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context



class SuccessView(TemplateView):
    template_name = "empleados/success.html"


class CreateEmpleado(CreateView):
    model = Empleado
    template_name = "empleados/create.html"
    #agregar campos por separado en la variable "form" que almacena todos los campos
    #fields = ['first_name', 'last_name',  'image', 'job', 'departamento','Habilidades',]

    #Se esta trabajando con formulario personalizado
    form_class = EmpleadoForm

    #agregar todos los campos
    #fields = ('__all__')

    #success_url = 'employees' #poner . regresa a la misma pagina una ves guardado esto se puede pero no es una buena practrica
    success_url = reverse_lazy('employee_app:empleados') #se utiliza la funcion reverse_lazy de django  y el nombre de url asignado

    #metodo para interseptar el guardado y validar campos
    #la variable form almacena lo enviado desde el formulario
    def form_valid(self, form):
        empleado = form.save(commit=False) #se crea una instancia de lo que se guardara en bd
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(CreateEmpleado, self).form_valid(form)
    

class UpdateEmpleado(UpdateView):
    model = Empleado
    template_name = "empleados/edit.html"
    fields = ['first_name', 'last_name', 'job', 'image','departamento','Habilidades']
    success_url = reverse_lazy('employee_app:empleados')

    # realizar un procesi previo al actualizado 
    #el post se ejecura antes que el form_valid no importa el orden en que se ponga
    #Aqui todavia no se validan los datos
    def post(self, request, *args, **kwargs):
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
        
    #esto se ejecuta una vez que se valida que los datos sean correctos 
    def form_valid(self, form):
        empleado = form.save(commit=False) #se crea una instancia de lo que se guardara en bd
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(UpdateEmpleado, self).form_valid(form)


class deleteEmpleado(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('employee_app:empleados')

    def delete(self, request, *args,  **kwargs) :
        self.object = self.get_object()
        print( self.object)      
        self.object.delete()
        return super().delete(request, *args, **kwargs)
