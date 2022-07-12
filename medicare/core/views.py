from urllib import request
from django.shortcuts import render
from .models import paciente
from .forms import ContactoForm, pacienteForm, Contacto

# Create your views here.

def home(request):
    data={
        'form': ContactoForm()
    }
    return render(request, 'core/home.html', data)

#formulario paciente
def form_paciente(request):
    data={
        'form': pacienteForm()
    }
    #Capturar los datos que se envía hacia la base de datos
    if request.method == 'POST':
        formulario = pacienteForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Paciente registrado."
        else:
            data["form"] = formulario
    return render(request, 'core/form_paciente.html', data)


#formulario paciente
def Contacto(request):
    data={
        'form': ContactoForm()
    }
    #Capturar los datos que se envía hacia la base de datos
    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registrado."
        else:
            data["form"] = formulario
    return render(request, 'core/home.html', data)


#Imprimir listado de pacientes
def listar_pacientes(request):
    pacientes= paciente.objects.all()
    dato = {
        'pacientes' : pacientes
    }    
    return render(request, 'core/pacientes.html',dato)

