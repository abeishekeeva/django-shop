from __future__ import absolute_import, unicode_literals
from .models import Order
from celery import shared_task
from django.template.loader import render_to_string

@shared_task
def notify_user_on_order(order_id):
    print('TEST!!!')
    order = Order.objects.get(id=order_id)  #ORM 
    subject = 'Thank you for your order!'
    html_message = render_to_string('order/order_email.html', {'order': instance})
    plain_message = strip_tags(html_message)
    from_email = 'From <shop@tmart.com>'
    to = [instance.user.email]

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message, fail_silently=True)



