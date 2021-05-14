from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# @receiver(post_save, sender=Order)
# def notify_user_on_order(sender, instance, **kwargs):    
#     if instance.paid != False or instance.user.email is None:     
#         pass 
#     else: 
#         subject = 'Thank you for your order!'
#         html_message = render_to_string('order/order_email.html', {'order': instance})
#         plain_message = strip_tags(html_message)        
#         from_email = 'From <from@example.com>'
#         to = 'to@example.com'

#         mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message, fail_silently=True)

