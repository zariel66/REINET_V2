from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Ubicacion(models.Model):
    idubicacion = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=45)
    ciudad = models.CharField(max_length=45)
    abreviatura = models.CharField(max_length=45)

    class Meta:
        db_table = 'Ubicacion'


class Perfil(User):
    idperfil = models.AutoField(primary_key=True)
    cedula = models.CharField(unique=True, max_length=10)
    foto = models.TextField()
    web = models.CharField(max_length=100)
    telefono = models.CharField(max_length=16)
    fecharegistro = models.DateTimeField()
    ipregistro = models.CharField(max_length=15)
    reputacion = models.DecimalField(max_digits=4, decimal_places=0)
    estado = models.IntegerField()
    privacidad = models.CharField(max_length=11)
    fkubicacion = models.ForeignKey(Ubicacion)

    class Meta:
        db_table = 'Perfil'


class Institucion(models.Model):
    idinstitucion = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45)
    siglas = models.CharField(max_length=12)
    logo = models.TextField()
    descripcion = models.CharField(max_length=500)
    mision = models.CharField(max_length=500)
    ubicacion = models.CharField(max_length=45)
    web = models.CharField(max_length=45)
    recursosofrecidos = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'Institucion'


class Membresia(models.Model):
    idmembresia = models.AutoField(primary_key=True)
    esadministrator = models.IntegerField()
    cargo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    fecha = models.CharField(max_length=45)
    ippeticion = models.CharField (max_length=45)
    estado = models.IntegerField(blank=True, null=True)
    fkinstitucion = models.ForeignKey(Institucion)
    fkusuario = models.ForeignKey(User)

    class Meta:
        db_table = 'Membresia'


class Mensaje(models.Model):
    idmensaje = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=1000)
    fecha = models.DateTimeField()
    asunto = models.CharField(max_length=45)
    fkemisor = models.ForeignKey(User,related_name='fkemisor')
    fkreceptor = models.ForeignKey(User,related_name='fkreceptor')

    class Meta:
        db_table = 'Mensaje'


class Peticion(models.Model):
    idpeticion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=128)
    usado = models.IntegerField()
    fkusuario = models.ForeignKey(User)

    class Meta:
        db_table = 'Peticion'

