from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=100)  

