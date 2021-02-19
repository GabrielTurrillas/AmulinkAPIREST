from django.contrib import admin
from .models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidoMaterno', 'apellidoPaterno', 'telefono', 'email')
    list_per_page = 25

admin.site.register(Paciente, PacienteAdmin)

