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
    idPac= models.IntegerField(primary_key=True, verbose_name= 'Id del paciente')
    nombrePac= models.CharField(max_length=25, verbose_name='Nombre del paciente')
    apellidoPac= models.CharField(max_length=35, verbose_name='Apellido del paciente')
    runPac= models.CharField(max_length=10, verbose_name='Rut del paciente')
    telefonoPac= models.IntegerField(verbose_name='Teléfono del paciente')
    correoPac= models.CharField(max_length=40, verbose_name='Correo del paciente')
    
    def __str__(self):
        return self.nombrePac + ' ' + self.apellidoPac
    

opcion_consutas = [
    [0, "Agendar"],
    [1, "Cancelar"],
    [2, "Reprogramar"]
]    


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=35, verbose_name='Apellido del cliente')
    correo = models.EmailField()
    telefonoPac= models.IntegerField(verbose_name='Teléfono del cliente')
    tipo_consulta= models.IntegerField(choices=opcion_consutas)
    mensaje= models.TextField()
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido
    