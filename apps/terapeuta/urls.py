from django .urls import path
from .views import listPerfilTerapeutaView, retrievePerfilTerapeutaView, updatePerfilTerapeutaView

urlpatterns = [
    path('listPerfilTerapeuta', listPerfilTerapeutaView),           # [TESTEADO CON POSTMAN]
    path('retrievePerfilTerapeuta', retrievePerfilTerapeutaView),   # [TESTEADO CON POSTMAN]
    path('updatePerfilTerapeuta', updatePerfilTerapeutaView)        # [TESTEADO CON POSTMAN]
]

# [MODIFICADO] de /admin/perfiles a listPerfilTerapeuta
# [MODIFICADO] de modificar_perfil a updatePerfilTerapeuta
# [MODIFICADO] de /perfil a retrievePerfilTerapeuta
