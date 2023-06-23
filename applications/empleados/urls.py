from django.urls import path
#from django.conf.urls.static import static

#Importando ruta del la vista(controlador) a las rutas
from . import views

app_name = "employee_app"

urlpatterns = [
    path('employees/', views.ListEmployees.as_view(), name='empleados'),
    #ruta con parametros
    path('employees-by-area/<short_name>', views.ListByArea.as_view(), name='employeesByArea'),

    path('search-employee', views.ListByKword.as_view()),
    path('skills-employee', views.ListHabilidades.as_view()),
    path('details-employee/<pk>', views.EmpleadoDetailView.as_view(), name='show'),
    path('create-employee', views.CreateEmpleado.as_view(), name='store'),
    path('update-employee/<pk>', views.UpdateEmpleado.as_view(),  name='update'),
    path('delete-employee/<pk>', views.deleteEmpleado.as_view(), name='destroy'),
    path('success', views.SuccessView.as_view(), name='correcto'),
]