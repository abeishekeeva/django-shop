from django.shortcuts import render, get_object_or_404, redirect
<<<<<<< HEAD
from .cart import Cart
from shop.models import Product
from .forms import ProductAddForm

# Create your views here.
=======
from .cart import Cart 
from shop.models import Product 
from .forms import ProductAddForm
from django.views.decorators.http import require_POST

>>>>>>> 1cd8cb2885fa20310957184f0f67ba12858b7678

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = ProductAddForm(initial={
<<<<<<< HEAD
                                            'quantity': item['quantity'],
                                            'override': True
                                            })
        print(item)
    return render(request, 'cart/cart.html', {'cart': cart})

def cart_add_from_main(request, product_id):
    cart = Cart(request)
    # product = get_object_or_404(Product, id=product_id)
    product = Product.objects.get(pk=product_id)
    cart.add(product)
    return redirect('cart:cart_detail')

def cart_add_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, product_id=id)
    form = ProductAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product, quantity = cd['quantity'], override_quantity=cd[override])

    return redirect('cart:cart_detail')

def remove_item_from_cart(request, product_id):
    cart = Cart(request)
    # product = get_object_or_404(Product, product_id)
    product = Product.objects.get(pk=product_id)
    cart.remove(product)
=======
        'quantity': item['quantity'],
        'override': True})              
    return render(request, 'cart/cart.html', {'cart': cart})


def cart_add_from_main(request, product_id):
    cart = Cart(request)    
    product = get_object_or_404(Product, id=product_id)    
    cart.add(product)
    return redirect('cart:cart_detail')

@require_POST
def cart_add_product(request, product_id):
    cart = Cart(request)
    
    product = get_object_or_404(Product, id=product_id)        
    form = ProductAddForm(request.POST)
    
    if form.is_valid(): 
        cd = form.cleaned_data
        cart.add(product, quantity=cd['quantity'], override_quantity=cd['override'])
        
>>>>>>> 1cd8cb2885fa20310957184f0f67ba12858b7678
    return redirect('cart:cart_detail')

def cart_delete_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

<<<<<<< HEAD
def product_detail():

    form = ProductAddForm()

    return render({'form': form})

    


  
=======
>>>>>>> 1cd8cb2885fa20310957184f0f67ba12858b7678

