from django.db import models
from app.models import Cliente, Complejo


# Create your models here.

class Consulta(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='cliente', on_delete=models.PROTECT, null=True)
    complejo = models.ForeignKey(Complejo, related_name='complejo', on_delete=models.PROTECT, null=True)
    mensaje = models.TextField(max_length=1000)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    cantidad_mayores = models.SmallIntegerField()
    cantidad_menores = models.SmallIntegerField()
    leida = models.BooleanField(null=True, blank=True, default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


    def __int__(self):
        return self.pk
    