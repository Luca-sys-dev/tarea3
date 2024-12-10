from django.db import models

# Create your models here.

class Consecionario(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40)
    marca = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.direccion} - {self.marca}"

class Vehiculo(models.Model):
    marca = models.CharField(max_length=20)
    anio = models.IntegerField()
    modelo = models.CharField(max_length=20)
    patente = models.CharField(max_length=7)
    valor = models.IntegerField()
    kilometraje = models.IntegerField()

    def __str__(self):
        return f"{self.marca} - {self.anio} - {self.modelo} - {self.patente} - {self.valor} - {self.kilometraje}"

class Agente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    edad = models.IntegerField()
    sueldo = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.dni} - {self.edad} - {self.sueldo}"