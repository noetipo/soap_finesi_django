from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer,EstudianteSerializer,PagosSerializer,ConsultaSerializer
from .models import *
from rest_framework import routers, serializers, viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class EstudianteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    #parser_classes = (XMLParser,)

    #renderer_classes = (XMLRenderer,)


class PagosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer

class EstudianteList(APIView):
    def get(self, request, format=None):
        snippets = Estudiante.objects.all()
        serializer = EstudianteSerializer(snippets, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = EstudianteSerializer(data=request.data)

        if serializer.is_valid():
            title = request.POST.get('nombre'),

            print(request.data['nombre'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ConsultaApi(APIView):
    parser_classes = (XMLParser,)

    renderer_classes = (XMLRenderer,)

    def post(self, request, format=None):

        serializer = ConsultaSerializer(data=request.data)

        if serializer.is_valid():


            print(request.data['dni'])
            pagos=Pagos.objects.filter(estudiante__dni=request.data['dni'])
            serializerPago=PagosSerializer(pagos, many=True)
            return Response(serializerPago.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)