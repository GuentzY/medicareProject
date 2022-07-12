from urllib import request
from django.shortcuts import render
from .models import paciente
from .forms import pacienteForm

# Create your views here.

def home(request):
    pacientes= paciente.objects.all()
    datos = {
        'pacientes' : pacientes
    }
    return render(request, 'core/home.html', datos)

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




def listar_pacientes(request):
    pacientes= paciente.objects.all()
    dato = {
        'pacientes' : pacientes
    }    
    return render(request, 'core/pacientes.html',dato)

