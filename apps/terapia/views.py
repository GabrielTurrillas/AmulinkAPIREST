import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ..paciente.models import Paciente
from ..paciente.serializers import PacienteSerializer
from .serializers import TerapiaSerializer, SesionSerializer
from .models import Terapia, Sesion

@api_view(['GET',])
def listTerapiaView(request):
    try:
        terapias = Terapia.objects.all()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TerapiaSerializer(terapias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET',])
@permission_classes([IsAdminUser])
def listTerapiaTerapeutaView(request):
    try:
        terapias = Terapia.objects.filter(userAccount=request.user)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TerapiaSerializer(terapias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
 

@api_view(['GET',])
def retrieveTerapiaView(request, pk): # MODIFICADO terapiaDetailView
    try:
        terapia = Terapia.objects.get(paciente=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TerapiaSerializer(terapia)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)    


@api_view(['POST',])
def createTerapiaView(request):
    if request.method == 'POST':
        serializer = TerapiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_METHOD_NOT_ALLOWED)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT',])
@permission_classes([IsAdminUser])
def updateTerapiaView(request, pkTerapia):
    try:
        terapia = Terapia.objects.get(pk=pkTerapia)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = TerapiaSerializer(terapia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(['GET',])
@permission_classes([IsAdminUser])
def listSesionAllView(request):
    try:
        sesiones = Sesion.objects.all()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SesionSerializer(sesiones, many=True)
        return Response(serializer.data)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET',])
@permission_classes([IsAdminUser])
def listSesionTerapeutaView(request):
    try:
        sesiones = Sesion.objects.filter(terapia__userAccount=request.user)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SesionSerializer(sesiones, many=True)
        return Response(serializer.data)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET',])
def listSesionView(request, pkPaciente):
    try:
        sesiones = Sesion.objects.filter(terapia__paciente__id=pkPaciente , terapia__userAccount=request.user)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SesionSerializer(sesiones, many=True)
        return Response(serializer.data)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET',])
def retrieveSesionView(request, pkSesion):
    try:
        sesion = Sesion.objects.get(id=pkSesion)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SesionSerializer(sesion)
        return Response(serializer.data)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST',])
def createSesionView(request):
    if request.method == 'POST':
        serializer = SesionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT',])
def updateSesionView(request, pkSesion):
    try:
        sesion = Sesion.objects.get(id=pkSesion)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SesionSerializer(sesion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)        


@api_view(['GET',])
def showCountSesionesMonthView(request):
    try:
        CountSesionesMonth = Sesion.objects.filter(terapia__userAccount=request.user, fechaSesion__gte=datetime.datetime.today().replace(day=1, hour=0, minute=0, second=0, microsecond=0)).count()
    except CountSesionesMonth.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(CountSesionesMonth)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

    

    

        
        
