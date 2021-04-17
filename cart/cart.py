from decimal import Decimal

from django.conf import settings

class Cart:

    def __init__(self,request):
        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)
        if cart is None:
            cart = self.session[settings.CART_SESSION_ID] ={}
        self.cart = cart

    def add(self,product,quantity=1 , override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price':str(product.price), 'name': str(product.name)}
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
        for product in products.values():
            total_quantity += product['quantity']

        return  total_quantity

    def __iter__(self):
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
        item['total_price'] = item['price'] * item['quantity']
        yield item

    def total_price(self):
        total_price = 0
        products = self.cart
        for product in products.values():
            total_price += product ['quantity'] * product['price']
        return total_price


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()