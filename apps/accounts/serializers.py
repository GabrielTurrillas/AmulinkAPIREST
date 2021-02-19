from djoser.serializers import UserCreateSerializer
from rest_framework.serializers import PrimaryKeyRelatedField
from django.contrib.auth import get_user_model
from ..terapia.models import Terapia
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    terapia = PrimaryKeyRelatedField(many=True, queryset=Terapia.objects.all())
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'name', 'password', 'terapia')