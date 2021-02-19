import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from ..paciente.models import Paciente
from ..paciente.serializers import PacienteSerializer
from .serializers import TerapiaSerializer, SesionSerializer
from .models import Terapia, Sesion


@api_view(['GET',])
def terapiaDetailView(request, pk):
    try:
        terapia = Terapia.objects.get(paciente=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TerapiaSerializer(terapia)
        return Response(serializer.data)

        

@api_view(['POST',])
def createTerapiaView(request):
    if request.method == 'POST':
        serializer = TerapiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT',])
@permission_classes([IsAdminUser])
def putTerapiaView(request, pk):
    try:
        terapia = Terapia.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = TerapiaSerializer(terapia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


    


@api_view(['GET','POST'])
def sesionListView(request, pk):
    if request.method == 'GET':
        sesiones = Sesion.objects.filter(terapia__paciente__id=pk, terapia__userAccount=request.user)
        serializer = SesionSerializer(sesiones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SesionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def sesionDetalleView(request, pk):
    if request.method == 'GET':
        sesion = Sesion.objects.get(id=pk)
        serializer = SesionSerializer(sesion)
        return Response(serializer.data)


@api_view(['PUT',])
def putSesionView(request, pk):
    try:
        sesion = Sesion.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SesionSerializer(sesion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


@api_view(['GET',])
def sesionCurrentMonthCountView(request):
    try:
        sesionCurrentMonthCount = Sesion.objects.filter(terapia__userAccount=request.user, fechaSesion__gte=datetime.datetime.today().replace(day=1, hour=0, minute=0, second=0, microsecond=0)).count()
    except sesionCurrentMonthCount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(sesionCurrentMonthCount)


"""     Order.objects.filter(created_at__gte=datetime.datetime.today().replace(day=1, hour=0, minute=0, second=0, microsecond=0)).count() """
    
    

    

        
        
