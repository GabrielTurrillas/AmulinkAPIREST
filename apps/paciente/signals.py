""" import getpass
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.accounts.models import UserAccount
from .models import Paciente, Terapia


@receiver(post_save, sender=Paciente)
def create_terapia(sender, instance, created, **kwargs):
    currentLoggedUserName = getpass.getuser()
    print(currentLoggedUserName)
    currentLoggedUserInstance = UserAccount.objects.get(name=currentLoggedUserName)
    if created:
        Terapia.objects.create(paciente=instance, userAccount=currentLoggedUserInstance)

@receiver(post_save, sender=Paciente)
def save_terapia(sender, instance, **kwargs):
    instance.paciente.save() """