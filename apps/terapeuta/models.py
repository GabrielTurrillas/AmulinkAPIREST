from datetime import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..accounts.models import UserAccount

class PerfilTerapeuta(models.Model):
    tipoCuenta_choise = (
        ('equipoInterno','equipoInterno'),
        ('equipoExterno','equipoExterno'),
        ('director','director'),
        ('pasante','pasante'),
    )
    userAccount = models.OneToOneField(UserAccount, related_name='perfilTerapeuta' ,on_delete=models.CASCADE)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fechaNacimiento = models.DateTimeField(null=True, blank=True)
    tipoCuenta = models.CharField(max_length=15, choices=tipoCuenta_choise, null=True)
        
    def __str__(self):
        return self.nombre

    









