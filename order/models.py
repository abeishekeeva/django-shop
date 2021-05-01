from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

# Create your models here.

class Order(models.Model): #one to one
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):

        return sum(item[price]*item[quantity] for item in self.items)

class OrderItem(models.Model): #One to many
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Ordering {self.id} - Order {self.oreder.id}"

    def get_cost(self):
        return self.price*self.quantity
