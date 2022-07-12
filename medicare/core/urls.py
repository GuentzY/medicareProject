from django.urls import path
from .views import home, form_paciente, listar_pacientes

urlpatterns = [
    path('',home, name= "home"),
    path('form-paciente', form_paciente, name="form_paciente"),
    path('listar-pacientes/', listar_pacientes, name="listar_pacientes"),
]
