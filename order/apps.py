from django.apps import AppConfig
from .signals import *

class OrderConfig(AppConfig):
    name = 'order'

    def reqady(self):
        import order.signals
