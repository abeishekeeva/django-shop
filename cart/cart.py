from shop import Product
from django.conf.settings import  CART_SESSION_ID

class Cart:

    def __init__(self,request,Product):
        self.session = request.session

        cart = self.session.get(CART_SESSION_ID)
        if cart is None:
            cart = self.session[CART_SESSION_ID] ={}
        self.cart = cart

    def add(self,product,quantity=1 , override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price':str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity

        else:
            self.cart[product_id]['quantity'] +=1

            silf.save()
    def save(self):
        self.session.modified =True

    def remove(self,product):
        product_id =str(product.id)
        if product_id in self.cart:
            del self.cart[product.id]

            self.save()

    def __len__(self):
        total_quantity = 0
        products = self.cart
        for product in products:
            total_quantity += product['quantity']

        return  total_quantity

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()