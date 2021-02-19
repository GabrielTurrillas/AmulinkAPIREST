from django .urls import path
from .views import terapiaDetailView, sesionListView, sesionDetalleView, sesionCurrentMonthCountView, createTerapiaView, putSesionView, putTerapiaView

urlpatterns = [
    path('<int:pk>', terapiaDetailView),
    path('admin/create_terapia', createTerapiaView),
    path('admin/put_terapia/<int:pk>', putTerapiaView),
    path('sesion/<int:pk>', sesionListView),
    path('sesion/sesion_detalle/<int:pk>', sesionDetalleView),
    path('sesion/contar_sesiones_mes', sesionCurrentMonthCountView),
    path('sesion/put_sesion/<int:pk>', putSesionView),
]