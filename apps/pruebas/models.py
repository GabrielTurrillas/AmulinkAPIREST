from django.db import models

# Create your models here.
class Prueba(models.Model):
    tipoTerapia_choise = (
        ('Isapre', 'Isapre'),
        ('Fonasa', 'Fonasa'),
        ('Bajo Costo', 'Bajo Costo'),
    )
    tipoTerapia = models.CharField(max_length=30, blank=True, null=True, choices=tipoTerapia_choise)