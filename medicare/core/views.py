from urllib import request
from django.shortcuts import render
from .models import paciente

# Create your views here.

def home(request):
    pacientes= paciente.objects.all()
    
    datos = {
        'pacientes' : pacientes
    }
    
    return render(request, 'core,home.html', datos)