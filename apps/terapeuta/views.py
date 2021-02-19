from .models import PerfilTerapeuta
from .serializers import PerfilTerapeutaSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status


class ListPerfilTerapeuta(ListAPIView):
    """ Para el admin """
    serializer_class = PerfilTerapeutaSerializer
    queryset = PerfilTerapeuta.objects.all()
    permission_classes = [IsAdminUser]


@api_view(['GET', ])
def getPerfilTerapeutaView(request):
    try:
        perfilTerapeuta = PerfilTerapeuta.objects.get(userAccount=request.user)
    except perfilTerapeuta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PerfilTerapeutaSerializer(perfilTerapeuta)
        return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAdminUser])
def getPerfilTerapeutaListView(request):
    try:
        perfiles = PerfilTerapeuta.objects.all()
    except perfiles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PerfilTerapeutaSerializer(perfiles, many=True)
        return Response(serializer.data)




@api_view(['PUT', ])
def putPerfilTerapeutaView(request):
    try:
        perfilTerapeuta = PerfilTerapeuta.objects.get(userAccount=request.user)
    except perfilTerapeuta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = PerfilTerapeutaSerializer(perfilTerapeuta, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"]= "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





        
    


