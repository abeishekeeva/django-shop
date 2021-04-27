<<<<<<< HEAD
from .cart import Cart

def cart(request):
    cart= Cart(request)
=======
from .cart import Cart 

def cart(request):
    cart = Cart(request)
>>>>>>> 1cd8cb2885fa20310957184f0f67ba12858b7678
    return {'cart': cart}