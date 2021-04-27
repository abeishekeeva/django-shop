from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator
from cart.forms import ProductAddForm


def product_list(request, category_slug=None): 

    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request,'shop/product_list.html',
        {'category': category,
        'categories': categories,
        'products': products})
        

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'shop/product-detail.html', {'product': product})


def contact_list(request):
    return render(request, 'shop/contact.html')

