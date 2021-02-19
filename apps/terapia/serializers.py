from rest_framework.serializers import ModelSerializer
from .models import Terapia, Sesion
from ..accounts.models import UserAccount

class TerapiaSerializer(ModelSerializer):
    class Meta:
        model = Terapia
        fields = '__all__'

class SesionSerializer(ModelSerializer):
    class Meta:
        model = Sesion
        fields = '__all__'