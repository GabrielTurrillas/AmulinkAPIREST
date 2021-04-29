from django.core.exceptions import ObjectDoesNotExist
from .models import PerfilTerapeuta
from .serializers import PerfilTerapeutaSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET',])
def listPerfilTerapeutaView(request):
    try:
        perfilTerapeuta = PerfilTerapeuta.objects.all()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PerfilTerapeutaSerializer(perfilTerapeuta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET',])
def retrievePerfilTerapeutaView(request):
    try:
        perfilTerapeuta = PerfilTerapeuta.objects.get(userAccount=request.user)
    except perfilTerapeuta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PerfilTerapeutaSerializer(perfilTerapeuta)
        return Response(serializer.data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT', ])
def updatePerfilTerapeutaView(request):
    try:
        perfilTerapeuta = PerfilTerapeuta.objects.get(userAccount=request.user)
    except perfilTerapeuta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = PerfilTerapeutaSerializer(perfilTerapeuta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)





        
    


