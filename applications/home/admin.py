from django.contrib import admin
from .models import Book

# Register your models here.


#Desde este archivo se puede interactuar con la base de datos

admin.site.register(Book)