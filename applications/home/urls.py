from django.urls import path
#Importando ruta del la vista(controlador) a las rutas
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('list/', views.ModelListBooks.as_view()),
    path('create-book/', views.CreateBook.as_view()),
]