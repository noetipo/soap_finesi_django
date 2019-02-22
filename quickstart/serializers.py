from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

from rest_framework import serializers


class ConsultaSerializer(serializers.Serializer):
    dni = serializers.IntegerField()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = (
            'id', 'nombre', 'apellido_paterno', 'dni', 'apellido_materno', 'correo', 'telefono', 'direccion',
            'created_at',
            'updated_at')





class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'id', 'nombre', 'created_at', 'updated_at')
class NotasCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotasCurso
        fields = (
            'id', 'estudiante', 'curso', 'nota', 'created_at', 'updated_at')
class ConsultaNotasCursoSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True)
    estudiante = EstudianteSerializer(read_only=True)
    class Meta:
        model = NotasCurso
        fields = (
            'id', 'estudiante', 'curso', 'nota', 'created_at', 'updated_at')

