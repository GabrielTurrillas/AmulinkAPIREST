from django.apps import AppConfig

class TerapeutaConfig(AppConfig):
    name = 'apps.terapeuta'

    def ready(self):
        import apps.terapeuta.signals
