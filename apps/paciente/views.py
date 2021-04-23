from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from ..terapia.models import Terapia
from ..accounts.models import UserAccount
from .models import Paciente
from .serializers import PacienteSerializer
from .permissions import PermisoTerapiaPaciente

# PacienteListCreateView, Clase eliminada remplasada por pacienteCreateView y pacienteListView
# PacienteView, Clase eliminada remplasada por updatePacienteView, retrievePacienteView
# PacienteAdminView Clase eliminada

@api_view(['GET',])
#@permission_classes([IsAdminUser])
def listPacienteView(request): 
    try:
        pacientes = Paciente.objects.all()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET',])
@permission_classes([IsAuthenticated])
def retrievePacienteView(request,pk): 
    try:
        instanciaPaciente = Paciente.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PacienteSerializer(instanciaPaciente)
        return Response(serializer.data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST',])
@permission_classes([IsAdminUser]) 
def createPacienteView(request):
    if request.method == 'POST':
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT',])
@permission_classes([IsAdminUser])
def updatePacienteView(request,pk):  # putPacienteView, nombre funcion modificada
    try:
        instanciaPaciente = Paciente.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PacienteSerializer(instanciaPaciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED) 
        


@api_view(['GET',])
@permission_classes([IsAuthenticated])
def listTerapeutaPacienteView(request):
    try:
        pacientes = Paciente.objects.filter(userAccount=request.user)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)





