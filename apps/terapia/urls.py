from django .urls import path
from .views import listTerapiaView, retrieveTerapiaView, createTerapiaView, updateTerapiaView, listSesionAllView, listSesionView, listSesionTerapeutaView, retrieveSesionView, createSesionView, updateSesionView, showCountSesionesMonthView, listTerapiaTerapeutaView 

urlpatterns = [
    path('listTerapia', listTerapiaView),                       # [TESTEADO CON POSTMAN]
    path('listTerapiaTerapeuta', listTerapiaTerapeutaView), 
    path('retrieveTerapia/<int:pk>', retrieveTerapiaView),      # [TESTEADO CON POSTMAN]
    path('createTerapia', createTerapiaView),                   # [TESTEADO CON POSTMAN]
    path('updateTerapia/<int:pkTerapia>', updateTerapiaView),   # [TESTEADO CON POSTMAN]
    path('listSesion',  listSesionAllView ),                    # [TESTEADO CON POSTMAN]
    path('listSesionTerapeuta', listSesionTerapeutaView),       # [TESTEADO CON POSTMAN]
    path('listSesion/<int:pkPaciente>', listSesionView),        # [TESTEADO CON POSTMAN]
    path('retrieveSesion/<int:pkSesion>', retrieveSesionView),  # [TESTEADO CON POSTMAN]
    path('createSesion', createSesionView),                     # [TESTEADO CON POSTMAN]
    path('updateSesion/<int:pkSesion>', updateSesionView),      # [TESTEADO CON POSTMAN]
    path('showCountSesionesMonth', showCountSesionesMonthView), # [TESTEADO CON POSTMAN]
]


    # [MODIFICADO] de terapiaDetailView a retrieveTerapiaView
    # [MODIFICADO] de putTerapiaView a updateTerapiaView
    # [MODIFICADO] de sesion_detalle a retrieveSesionView
    # [MODIFICADO] de sesionLista a listSesionView
    # [NUEVO] createSesion
    # [MODIFICADO] de sesion/put_sesion/<int:pk> a updateSesion
    # [MODIFICADO] de sesion/contar_sesiones_mes a showCountSesionesMonth
