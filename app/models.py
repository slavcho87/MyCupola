from django.db import models

class Imagen(models.Model):
    """Imagenes de la NASA que tienen todos los usuarios en sus albumes"""
    direccion = models.CharField(max_length=200,primary_key=True)

class Album(models.Model):
    """Representa los albumes que tienen los usuarios"""
    nombre = models.CharField(max_length=10) 
    imagenes = models.ManyToManyField(Imagen, blank=True)

class Usuario(models.Model):
    """Representa los usuarios de la base de datos"""
    email = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=50)
    albumes = models.ManyToManyField(Album, blank=True)
    
class MeGusta(models.Model):
    usuario = models.ForeignKey(Usuario) 
    imagen = models.ForeignKey(Imagen)
