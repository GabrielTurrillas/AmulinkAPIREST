from django.contrib import admin
from .models import PerfilTerapeuta

class PerfilTerapeutaAdmin(admin.ModelAdmin):
    list_display = ('id', 'userAccount', 'rut', 'nombre', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'email', 'genero', 'fechaNacimiento' )
    list_per_page = 25



admin.site.register(PerfilTerapeuta, PerfilTerapeutaAdmin)