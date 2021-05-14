from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


class Order(models.Model): # One-To-One 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        return sum(item[price] * item[quantity] for item in self.items)


class OrderItem(models.Model): #One-To-Many 
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Orderitem {self.id} - Order {self.order.id}"
    
    def get_cost(self):
        return self.price * self.quantity 
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail
from django.core import  mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@receiver(post_save,sender=Order)
def notify_user_on_order(sender, instance, **kwargs):
    if instance.paid !=True or instance.user.email is None :
        print('Test')
        pass
    else:
        subject = 'Subject'
        # html_massage = render_to_string('mail_template.html', ('order':instance))
        # plain_massahe = strip_tags(html_massage)
        from_emaill = 'From <from@exaple.com>'
        to = 'to@exaple.com'

        mail.send_mail(subject,plain_massage,from_emaill,[to],html_massage=html_massage)




