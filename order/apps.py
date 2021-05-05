from django.apps import AppConfig
# from .signals import *
from django.utils.translation import ugettext_lazy as _

class OrderConfig(AppConfig):
    name = 'order'
    verbose_name = _('order') 

    def ready(self):
        import order.signals
