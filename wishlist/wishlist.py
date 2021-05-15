from shop.models import Product 
from django.conf import settings

class Wishlist: 

    def __init__(self, request):
        self.session = request.session 
        
        wishlist = self.session.get(settings.WISHLIST_SESSION_ID) #None, если корзины нет
        if wishlist is None: 
            wishlist = self.session[settings.WISHLIST_SESSION_ID] = {} #{'CART': {}}
        self.wishlist = wishlist 
    
    
    def add(self, product, quantity=1, override_quantity=False):
        
        product_id = str(product.id) 
        if product_id not in self.wishlist: 
            self.wishlist[product_id] = {'quantity': 0, 
                                    'price': str(product.price)}
        if override_quantity: 
            self.wishlist[product_id]['quantity'] = quantity
        else:
            self.wishlist[product_id]['quantity'] += 1 
                            
        self.save()

    def remove(self, product): 
        product_id = str(product.id)
        if product_id in self.wishlist:
            del self.wishlist[product.id]        
            self.save()
    
    def clear(self):
        del self.session[settings.WISHLIST_SESSION_ID]
        self.save()        

    def __len__(self):
        total_quantity = 0 
        products = self.wishlist
        for product in products: 
            total_quantity += product['quantity']
        
        return total_quantity

    def total_price(self):
        total_price = 0
        products = self.wishlist 
        for product in products:
            total_price += product['quantity'] * product['price'] 
        
        return total_price


    def save(self): 
        self.session.modified = True 