from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from shop.models import Product
from .forms import ProductAddForm


def cart_detail(request):
    cart= Cart(request)
    return render(request, 'cart/cart.html',{"cart":cart})

def cart_add_form_main(request, product_id):
    cart= Cart(request)
    product= Product.objects.get(pk=product_id)
    return redirect('cart:cart_detail')

def cart_add_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, product_id)
    addProductForm = ProductAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
    cart.add(product, quantity=cd['quantity'], override_quantity=cd['override'])

    return redirect('cart:cart_detail')

