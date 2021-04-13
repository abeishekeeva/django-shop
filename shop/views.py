from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None): 
    request.session['foo'] = 'bar'
    print('test', request.session['foo'])
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,'shop/product_list.html',
        {'category': category,
        'categories': categories,
        'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/detail.html', {'product': product})