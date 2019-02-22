from uuid import UUID

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer,EstudianteSerializer,NotasCursoSerializer,ConsultaSerializer, CursoSerializer,ConsultaNotasCursoSerializer
from .models import *
from rest_framework import routers, serializers, viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
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

class CursoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer



class EstudianteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    #parser_classes = (XMLParser,)

    #renderer_classes = (XMLRenderer,)


class NotasCursoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = NotasCurso.objects.all()
    serializer_class = NotasCursoSerializer

class EstudianteList(APIView):
    permission_classes = (IsAuthenticated,)
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
    #parser_classes = (XMLParser,)

    #renderer_classes = (XMLRenderer,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):

        serializer = ConsultaSerializer(data=request.data)

        if serializer.is_valid():

            estudiante=Estudiante.objects.get(dni=request.data['dni'])
            notas=NotasCurso.objects.filter(estudiante__id=estudiante.id)
            serializerPago=ConsultaNotasCursoSerializer(notas, many=True)
            return Response(serializerPago.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)