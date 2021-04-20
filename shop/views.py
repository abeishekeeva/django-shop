from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator

<<<<<<< HEAD
def product_list(request, category_slug=None):
=======
def product_list(request, category_slug=None): 
     
>>>>>>> origin
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

<<<<<<< HEAD
    paginator = Paginator(products,2)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)


=======
    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

>>>>>>> origin
    return render(request,'shop/product_list.html',
        {'category': category,
        'categories': categories,
        'products': products})
        

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/detail.html', {'product': product})

<<<<<<< HEAD
def contact_list(request):
    return render(request, 'shop/contact.html')
=======



>>>>>>> origin
