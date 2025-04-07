from django.apps import AppConfig


class ItassetsConfig(AppConfig):
    name = 'itassets'

    def ready(self):
        import itassets.signals
