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


class Pagos(models.Model):
    """
    docs
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, )
    importe = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True);

    dni = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        docs
        """
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    #def __str__(self):
     #   return self.estudiante
