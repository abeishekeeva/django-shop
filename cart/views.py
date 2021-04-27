from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart 
from shop.models import Product 
from .forms import ProductAddForm

# Create your views here.
def cart_detail(request):
    
    cart = Cart(request)
    for item in cart:
        print(item)
        item['update_quantity_form'] = ProductAddForm(initial={
                                            'quantity': item['quantity'],
                                            'override': True
                                        })
        print(item)
    print(cart)
    return render(request, 'cart/cart.html', {'cart': cart})

def cart_add_from_main(request, product_id):
    cart = Cart(request)
    # product = Product.objects.get(pk=product_id)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect('cart:cart_detail')

def cart_add_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, product_id)
    form = ProductAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product, quantity=cd['quantity'], override_quantity=cd['override'])
                                        
    return redirect('cart:cart_detail')


def delete_from_cart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(pk=product_id)
    # product = get_object_or_404(Product, product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
