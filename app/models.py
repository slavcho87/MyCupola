from django.db import models

class Usuario(models.Model):
    """Representa los usuarios de la base de datos"""
    email = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=50)
    nombre = models.CharField(max_length=20)


