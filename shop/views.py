from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator





def product_list(request, category_slug=None): 
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request,'shop/product_list.html',
        {'category': category,
        'categories': categories,
        'products': products})
        

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        print(item)
        item['update_quantity_form'] = ProductAddForm(initial={
                                            'quantity': item['quantity'],
                                            'override': True
                                            })
        print(item)
    return render(request, 'cart/cart.html', {'cart': cart})        

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    for item in product:
        item['update_quantity_form'] = ProductAddForm(initial={
                                                'quantity': item['quantity'],
                                                'override': True
                                                })
    return render(request, 'shop/detail.html', {'product': product})

def contact(request):
    return render(request, 'shop/contact.html', {'contact': contact})


def portfolio(request):
    return render(request, 'shop/portfolio.html', {'portfolio': portfolio})

def blog(request):
    return render(request, 'shop/blog.html', {'blog': blog})


   