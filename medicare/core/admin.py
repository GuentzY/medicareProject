from django.contrib import admin
from .models import doctor, paciente, Contacto

# Register your models here.
admin.site.register(doctor)
admin.site.register(paciente)
admin.site.register(Contacto)