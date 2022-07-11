from pyexpat import model
from django.db import models

# Create your models here.

#Modelo para doctor
class doctor(models.Model):
    idDoctor= models.IntegerField(primary_key=True, verbose_name='Id del doctor')
    nombreDoc= models.CharField(max_length=50, verbose_name='Nombre del doctor')
    
    
    def __str__(self):
        return self.nombreDoc


#Modelo para paciente
class paciente(models.Model):
    nombrePac= models.CharField(max_length=25, verbose_name='Nombre del paciente')
    apellidoPac= models.CharField(max_length=35, verbose_name='Apellido del paciente')
    runPac= models.CharField(max_length=10, verbose_name='Rut del paciente')
    telefonoPac= models.IntegerField(max_length=9, verbose_name='Teléfono del paciente')
    correoPac= models.CharField(max_length=20, verbose_name='Correo del paciente')