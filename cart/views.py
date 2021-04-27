
from django.shortcuts import render,get_object_or_404,redirect
from shop.models import Category, Product
from .forms import ProductAddForm
from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart 
<<<<<<< HEAD
=======
from shop.models import Product 
from .forms import ProductAddForm
from django.views.decorators.http import require_POST
>>>>>>> origin


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
<<<<<<< HEAD
        item['update_quantity_form'] = ProductAddForm(initial={'quantity': item['quantity'],
                                                               'override': True})

=======
        item['update_quantity_form'] = ProductAddForm(initial={
        'quantity': item['quantity'],
        'override': True})              
>>>>>>> origin
    return render(request, 'cart/cart.html', {'cart': cart})


def cart_add_from_main(request, product_id):
    cart = Cart(request)    
    product = get_object_or_404(Product, id=product_id)    
    cart.add(product)
    return redirect('cart:cart_detail')

<<<<<<< HEAD

=======
@require_POST
>>>>>>> origin
def cart_add_product(request, product_id):
    cart = Cart(request)
    
    product = get_object_or_404(Product, id=product_id)        
    form = ProductAddForm(request.POST)
<<<<<<< HEAD
    if form.is_valid():
=======
    
    if form.is_valid(): 
>>>>>>> origin
        cd = form.cleaned_data
        cart.add(product, quantity=cd['quantity'], override_quantity=cd['override'])
        
    return redirect('cart:cart_detail')

<<<<<<< HEAD
def cart_delete_item_id(request,product_id):
    cart = Cart(request)
    #product = get_object_or_404(Product, product_id)
    product = Product.objects.get(pk=product_id)
    cart.remove(product)
    return redirect(('cart:cart_detail'))
=======
def cart_delete_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


>>>>>>> origin
