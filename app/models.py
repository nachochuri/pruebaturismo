from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
#from django.utils.translation import ugettext_lazy as _
# Create your models here.

localidades = [
    [0, 'Atlántida'],
    [1, 'Colonia del Sacramento'],
    [2, 'Piriápolis'],
    [3, 'Punta Ballena'],
    [4, 'Punta del Diablo'],
    [5, 'Punta del Este'],
    [6, 'Salto']
]



class Equipamiento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Equipamiento')
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Complejo(models.Model):
    user = models.OneToOneField(User, related_name='complejo', on_delete=models.CASCADE, null=True)
    nombre_complejo = models.CharField(max_length=50)
    localidad = models.IntegerField(choices=localidades, null=True)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    activo = models.BooleanField(default=True)
    descripcion = models.TextField(max_length=1000)
    equipamiento = models.ManyToManyField(Equipamiento)
    imagen1 = models.ImageField(upload_to='complejos', null=True)
    imagen2 = models.ImageField(upload_to='complejos', null=True)
    imagen3 = models.ImageField(upload_to='complejos', null=True)
    imagen4 = models.ImageField(upload_to='complejos', null=True)
    imagen5 = models.ImageField(upload_to='complejos', null=True)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_complejo

    def ver_localidad(self):
        return self.localidad.display()
    

paises = [
    [0, 'Alemania'],
    [1, 'Argentina'],
    [2, 'Brasil'],
    [3, 'Chile'],
    [4, 'España'],
    [5, 'Italia'],
    [6, 'Uruguay']
]

class Cliente(models.Model):
    user = models.OneToOneField(User, related_name='cliente', on_delete=models.CASCADE, null=True)
    
    telefono = models.IntegerField()
    pais = models.IntegerField(choices=paises)
    avisos = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.user.username


class Servicio(models.Model):
    complejo = models.ForeignKey(Complejo, related_name='servicio', on_delete=CASCADE)
    agua_caliente = models.BooleanField(default=False)
    luz = models.BooleanField(default=False)
    calefaccion = models.BooleanField(default=False)
    calefon = models.BooleanField(default=False)
    lluveiro = models.BooleanField(default=False)
    mucama = models.BooleanField(default=False)
    desayuno = models.BooleanField(default=False)
    sabanas = models.BooleanField(default=False)
    toallas = models.BooleanField(default=False)
    lavandería = models.BooleanField(default=False)
    cafetería = models.BooleanField(default=False)
    sereno = models.BooleanField(default=False)
    vigilancia = models.BooleanField(default=False)

    def __str__(self):
        return self.complejo.nombre_complejo
    

class Exterior(models.Model):
    complejo = models.ForeignKey(Complejo, related_name='exterior', on_delete=CASCADE)
    piscina_climatizada = models.BooleanField(default=False)
    jardin = models.BooleanField(default=False)
    terraza = models.BooleanField(default=False)
    piscina = models.BooleanField(default=False)
    parrillero = models.BooleanField(default=False)
    parrillero_techado = models.BooleanField(default=False)
    estacionamiento = models.BooleanField(default=False)
    estacionamiento_techado = models.BooleanField(default=False)
    terreno_cercado = models.BooleanField(default=False)
    decks = models.BooleanField(default=False)
    vista_mar = models.BooleanField(default=False)
    sillas_playa = models.BooleanField(default=False)
    frente_mar = models.BooleanField(default=False)
    duchero_exterior = models.BooleanField(default=False)
    bicicletas = models.BooleanField(default=False)

    def __str__(self):
        return self.complejo.nombre_complejo