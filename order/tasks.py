from .models import Order 
from celery import shared_task 

@shared_task 
def notify_user_on_order(order_id):    
    order = Order.objects.get(id=order_id) #ORM 

    subject = 'Thank you for your order!'
    html_message = render_to_string('order/order_email.html', {'order': order})
    plain_message = strip_tags(html_message)        
    from_email = 'From <from@example.com>'
    to = 'to@example.com'

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message, fail_silently=True)