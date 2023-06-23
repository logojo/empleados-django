from django.urls import path
from . import views

app_name = "department_app"

urlpatterns = [
    path('index-department', views.ListDepartments.as_view(), name='departments'),
    path('create-department', views.CreateDepartment.as_view(), name='store')
]