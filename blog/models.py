from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    apodo = models.CharField(max_length=20)

class Administrador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

class Publicaciones(models.Model):
    titulo_de_publicacion = models.CharField(max_length=20)
    publicacion = models.CharField(max_length=200)
    fecha_de_publicacion = models.DateField()
