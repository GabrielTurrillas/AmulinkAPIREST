from django.urls import path
from .views import PacienteListCreateView, PacienteView, PacienteListView, PacienteAdminView, pacienteCreateView, pacienteListView, putPacienteView

urlpatterns = [
    path('', PacienteListView.as_view()),
    path('<int:pk>', PacienteView.as_view()),
    path('admin/create', pacienteCreateView),
    path('admin/list', pacienteListView),
    path('admin/<int:pk>', PacienteAdminView.as_view()),
    path('admin/putPaciente/<int:pk>', putPacienteView),
]