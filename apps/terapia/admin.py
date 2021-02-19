from django.contrib import admin
from .models import Terapia, Sesion

class TerapiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'userAccount', 'fechaInicio', 'motivoConsulta', 'captacion')
    list_per_page = 25

class SesionAdmin(admin.ModelAdmin):
    list_display = ('terapia', 'asistio', 'fechaSesion')
    list_per_page = 25
    

admin.site.register(Terapia, TerapiaAdmin)
admin.site.register(Sesion, SesionAdmin)