from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# @receiver(post_save, sender=Order)
# def notify_user_on_order(sender, instance, **kwargs):
#     # instance.updated_at is not None or
#     if instance.paid != False or instance.user.email is None:
#         print('TEST!!!!!')
#         pass 
#     else:
#         subject = 'Thank you for your order!'
#         html_message = render_to_string('order/order_email.html', {'order': instance})
#         plain_message = strip_tags(html_message)
#         from_email = 'From <shop@tmart.com>'
#         to = [instance.user.email]

#         mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message, fail_silently=True)


# @receiver(post_save, sender=Order)
# def notify_user_on_register(sender, instance, **kwargs):
#     subject = 'Welcome to TMART!'
#     html_message = render_to_string('order/registration_email.html', {'order': instance})
#     plain_message = strip_tags(html_message)
#     from_email = 'From <shop@tmart.com>'
#     to = [instance.user.imail]

#     mail.send_mail(sebject, plain_message, from_email, [to], html_message=html_message, fail_silently=True)
    
