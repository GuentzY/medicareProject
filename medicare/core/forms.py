from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Contacto, paciente

#clase paraf el formulario de la base de datos

class pacienteForm(ModelForm):
    
    class Meta:
        model= paciente
        #fields= ['nombre', 'apellido', 'rut', 'telefono', 'correo']
        fields = '__all__'
        
        
# Formulario de contacto

class ContactoForm(ModelForm):
    
    class Meta:
        model= Contacto
        fields = '__all__'
        
        