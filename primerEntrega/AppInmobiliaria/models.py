from django.db import models

# Create your models here.

class Casas(models.Model):
    direccion = models.CharField(max_length=200)
    numero = models.IntegerField()
    pisos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return self.direccion+" "+str(self.numero)
  

class Departamentos(models.Model):
    direccion = models.CharField(max_length=200)
    numero = models.IntegerField()
    pisos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    precio = models.IntegerField()
    expensas = models.IntegerField()

    def __str__(self):
        return self.direccion+" "+str(self.numero)

class Contactos(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return self.nombre+" "+self.apellido