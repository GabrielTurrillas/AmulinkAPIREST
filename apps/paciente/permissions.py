from rest_framework.permissions import BasePermission
from ..terapia.models import Terapia
from django.contrib.auth import get_user_model

User = get_user_model

class PermisoTerapiaPaciente(BasePermission):
    def has_object_permission(self, request, view, obj):
        instanciaTerapia = Terapia.objects.get(paciente=obj.id)
        return instanciaTerapia.userAccount == request.user
