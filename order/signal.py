from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail
from django.core import  mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@receiver(post_save,sender=Order)
def notify_user_on_order(sender, instance, **kwargs):
    if instance.updated_at is not None or instance.paid !=True or instance.user.email is None :
        pass
    else:
        subject = 'Subject'
        html_massage = render_to_string('mail_template.html', ('order':instance))
        plain_massahe = strip_tags(html_massage)
        from_emaill = 'From <from@exaple.com>'
        to = 'to@exaple.com'

        mail.send_mail(subject,plain_massahe,from_emaill,[to],html_massage=html_massage)




