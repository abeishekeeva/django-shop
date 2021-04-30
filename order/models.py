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