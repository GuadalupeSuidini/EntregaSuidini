from django.db import models

# Create your models here.


class Empleado(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    email = models.EmailField()
    dni = models.IntegerField()


class Cliente(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    dni = models.IntegerField()


class Proveedor(models.Model):

    cuit = models.IntegerField()
    razonSocial = models.CharField(max_length=50)
    email = models.EmailField()
