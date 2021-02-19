from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from ..accounts.models import UserAccount
from ..terapia.models import Terapia
from ..accounts.models import UserAccount
from .models import Paciente
from .serializers import PacienteSerializer
from .permissions import PermisoTerapiaPaciente

class PacienteListCreateView(ListCreateAPIView):
    serializer_class = PacienteSerializer
    pagination_class = None
    queryset = Paciente.objects.all()
    permission_classes = [IsAdminUser]


@api_view(['PUT',])
@permission_classes([IsAdminUser])
def putPacienteView(request,pk):
    try:
        instanciaPaciente = Paciente.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PacienteSerializer(instanciaPaciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status)



@api_view(['POST',])
@permission_classes([IsAdminUser])
def pacienteCreateView(request):
    if request.method == 'POST':
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET',])
@permission_classes([IsAdminUser])
def pacienteListView(request):
    try:
        pacientes = Paciente.objects.all()
    except pacientes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)


class PacienteView(RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermisoTerapiaPaciente]


class PacienteAdminView(RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAdminUser]


class PacienteListView(ListAPIView):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all
    pagination_class = None
    permission_classes = [PermisoTerapiaPaciente]

    def get_queryset(self):
        return Paciente.objects.filter(userAccount=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PacienteSerializer(queryset, many=True)
        return Response(serializer.data)




