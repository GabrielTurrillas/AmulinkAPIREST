from django.urls import path
from .views import  listPacienteView, retrievePacienteView, createPacienteView, updatePacienteView, listTerapeutaPacienteView

urlpatterns = [
    path('listPaciente', listPacienteView),                     # [TESTEADO CON POSTMAN]
    path('retrievePaciente/<int:pk>', retrievePacienteView),    # [TESTEADO CON POSTMAN]
    path('createPaciente', createPacienteView),                 # [TESTEADO CON POSTMAN]
    path('updatePaciente/<int:pk>', updatePacienteView),        # [TESTEADO CON POSTMAN]
    path('listTerapeutaPaciente', listTerapeutaPacienteView),   # [TESTEADO CON POSTMAN]
]

# path('admin/<int:pk>', PacienteAdminView.as_view()) REMPLAZADA
# path('admin/create', pacienteCreateView), MODIFICADA
# path('admin/list', pacienteListView) MODIFICADA
# path('admin/putPaciente/<int:pk>', putPacienteView) REMPLAZADA
# path('<int:pk>', PacienteView.as_view()) REMPLAZADA 
# path('', PacienteListView.as_view()) ELIMINADA