from django .urls import path
from .views import showNumeroHorasMesView, showNumeroPacientesView, showNumeroSesionesMensualesView, showNumeroPacientesActivosView,showNumeroSesionesAnualesView

urlpatterns = [
    path('showNumeroHorasMes', showNumeroHorasMesView),    # [TESTEADO CON POSTMAN]                                                             
    path('showNumeroPacientes', showNumeroPacientesView),   # [TESTEADO CON POSTMAN]
    path('showNumeroSesionesMensuales/<int:mes>/<int:año>', showNumeroSesionesMensualesView), # [TESTEADO CON POSTMAN]
    path('showNumeroPacientesActivos', showNumeroPacientesActivosView), # [TESTEADO CON POSTMAN]
    path('showNumeroSesionesAnuales/<str:prevision>/<int:terapeuta>/<int:año>', showNumeroSesionesAnualesView) # [testear con cliente]
]