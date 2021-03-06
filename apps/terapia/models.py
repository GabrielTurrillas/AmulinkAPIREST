from django.db import models
from ..paciente.models import Paciente
from ..accounts.models import UserAccount

class Terapia(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    userAccount = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    fechaInicio = models.DateTimeField(auto_now_add=True)


class Sesion(models.Model):
    modalidad_choice = (
        ('Presencial', 'Presencial'),
        ('Online', 'Online'),
    )
    terapia = models.ForeignKey(Terapia, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)
    asistio = models.BooleanField(default=False)
    fechaSesion = models.DateTimeField(blank=True, null=True)
    modalidad = models.CharField(max_length=30, blank=True, null=True, choises=modalidad_choice)
    notasSesion = models.TextField(blank=True, null=True)
    fechaPago = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-id']
    
