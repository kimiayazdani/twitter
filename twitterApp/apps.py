from django.apps import AppConfig
from django.apps import AppConfig


class TwitterappConfig(AppConfig):
    name = 'twitterApp'

    def ready(self):
        import twitterApp.signals
