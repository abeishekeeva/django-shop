from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart 
from shop.models import Product 
from .forms import ProductAddForm
from django.views.decorators.http import require_POST


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = ProductAddForm(initial={
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
        
    return redirect('cart:cart_detail')

def cart_delete_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


