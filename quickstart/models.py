from uuid import uuid4
from django.db import models


class Estudiante(models.Model):
    """
    docs
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    dni=models.IntegerField(null=True, blank=True)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        docs
        """
        verbose_name = "Estidante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        docs
        """
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre

class NotasCurso(models.Model):
    """
    docs
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, )
    curso= models.ForeignKey(Curso, on_delete=models.CASCADE, )
    nota = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        docs
        """
        verbose_name = "NotasCurso"
        verbose_name_plural = "NotasCursos"

    #def __str__(self):
     #   return self.estudiante
