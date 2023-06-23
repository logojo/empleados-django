from django.shortcuts import render
from .models import Book
from django.views.generic import CreateView
from .forms import BookForm

#Esto ya es una vista preparada por django para mostrarme HTML
#En django las views representan los controladores 
from django.views.generic import TemplateView, ListView  


#Clase que hereda del TemplateView de django
class IndexView(TemplateView):
    template_name = 'home/home.html'

class ListHome(ListView):
    template_name = 'home/list.html'
    queryset = ['A','B','C'] #arreglo a mandar al html (templete) se puede conectar funcion que consulte a BD
    context_object_name = 'lista' #variable con la que se leeran los datos en el templete

class ModelListBooks(ListView):
    model = Book
    template_name = 'home/list.html'
    context_object_name = 'lista'

class CreateBook(CreateView):
    model = Book
    template_name = "home/create.html"
    #fields = ('__all__')
    #Con esto vinculo el formulario creado al html
    form_class = BookForm
    success_url = '/list'
