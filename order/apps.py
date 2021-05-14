from django.apps import AppConfig
from .signals import *


class OrderConfig(AppConfig):
    name = 'order'

    def ready(self):
        import order.signals
