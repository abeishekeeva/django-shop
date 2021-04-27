
from django.shortcuts import render
from .wishlist import Wishlist
# Create your views here.

def wishlist_detail(request):
    wishlist = Wishlist(request)
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist})

# def wishlist_add_from_main(request, product_id):
#     wishlist = Wishlist(request)
#     # product = get_object_or_404(Product, product_id)
#     product = Product.objects.get(pk=product_id)
#     wishlist.add(product)
#     return redirect('cart:cart_detail')