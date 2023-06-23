from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import CreateDeparment

from applications.empleados.models import Empleado
from .models import Departamento


class ListDepartments(ListView):
    template_name = "departamentos/index.html"
    context_object_name = 'departamentos'
    paginate_by =  5

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        departamentos = Departamento.objects.filter(
            name__icontains = kword
        )
        return departamentos


# Create your views here.
class CreateDepartment(FormView):
    template_name = 'departamentos/create.html'
    form_class = CreateDeparment
    success_url = '.'

    def form_valid(self, form):
        #instancia del modelo departamanto
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shortname']
        )

        depa.save()
        #Recuperando datos que vienen del formulario
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']

        #guardando empleado usando el modelo Empleados
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            job = 3,
            departamento = depa
        )
        return super(CreateDepartment, self).form_valid(form)
