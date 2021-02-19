from django .urls import path
from .views import ListPerfilTerapeuta, getPerfilTerapeutaView, putPerfilTerapeutaView, getPerfilTerapeutaListView

urlpatterns = [
    path('', ListPerfilTerapeuta.as_view()),
    path('perfil', getPerfilTerapeutaView),
    path('admin/perfiles', getPerfilTerapeutaListView),
    path('modificar_perfil', putPerfilTerapeutaView)
]