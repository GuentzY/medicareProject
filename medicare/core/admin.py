from django.contrib import admin
from .models import doctor, paciente

# Register your models here.
admin.site.register(doctor)
admin.site.register(paciente)