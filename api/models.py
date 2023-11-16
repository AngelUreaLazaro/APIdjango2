from email.headerregistry import Group
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=100)  

class DatosCSV(models.Model):
    Marca_temporal = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    pregunta1 = models.CharField(max_length=100)
    pregunta2 = models.CharField(max_length=100)
    pregunta3 = models.CharField(max_length=100)
    pregunta4 = models.CharField(max_length=100)
    pregunta5 = models.CharField(max_length=100)
    pregunta6 = models.CharField(max_length=100)
    pregunta7 = models.CharField(max_length=100)
    pregunta8 = models.CharField(max_length=100)
    pregunta9 = models.CharField(max_length=100)
    pregunta10 = models.CharField(max_length=100)
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name



