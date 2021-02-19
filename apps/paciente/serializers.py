from rest_framework import serializers
from .models import Paciente
from ..accounts.models import UserAccount

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
