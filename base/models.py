from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Local(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Socio(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField(null=True, default=None)
    email = models.EmailField()
    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Ocupacion(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField(null=True, default=None)
    email = models.EmailField()
    ocupacion = models.ForeignKey(Ocupacion, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Agenda(models.Model):
    fecha = models.DateTimeField(null=True, default=None)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.fecha)


