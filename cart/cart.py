from shop.models import Product
from django.conf import settings

class Cart:

    def __init__(self, request):
        self.session= request.session
        {'CART':{}}
        cart= self.session.get(settings.CART_SESSION_ID)
        if cart is None:
            cart= self.session[settings.CART_SESSION_ID]={'CART':{}}
        self.cart=cart

    def add(self, product, quantity=1, override_quantity=False):
        
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'price' : str(product.price)}
        if override_quantity: 
            self.cart[product_id] ['quantity'] = quantity
        else:
            self.cart[product_id] ['quantity'] += 1 

        self.save()

    def remove(self, product):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]

            self.save()

    def remove(self, product):
        product_id = str(product_id)

    def __len__(self):
        total_quantity = 0
        products = self.cart
        for product in products:
            total_quantity+=product['quantity'] 

        return total_quantity

    def total_price(self):
        total_price=0
        products = self.cart
        for product in products:
            total_price+=product['price']*product['quantity']
        return total_price
            

   
    def save(self):
        self.session.modified = True
    