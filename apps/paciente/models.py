from django.db import models
# Create your models here.

class Paciente(models.Model):
    prevision_choise = (
        ('Isapre', 'Isapre'),
        ('Fonasa', 'Fonasa'),
        ('Bajo Costo', 'Bajo Costo'),
    )
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    fechaNacimiento = models.DateTimeField(null=True, blank=True)
    genero = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    comunaResidencia = models.CharField(max_length=100) #hacerla con opciones
    ocupacionProfecion = models.CharField(max_length=50)
    prevision = models.CharField(max_length=30, blank=True, null=True, choices=prevision_choise)
    motivoConsulta = models.CharField(max_length=30, blank=True, null=True)
    captacion = models.CharField(max_length=30, blank=True, null=True)
    isActive = models.BooleanField(default=True)
    userAccount = models.ManyToManyField('accounts.UserAccount', through='terapia.Terapia')

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['-id']









