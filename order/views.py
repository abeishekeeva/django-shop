from django.shortcuts import render
from django.views import generic 
from .forms import OrderForm
from cart.cart import Cart 
from .models import OrderItem

class OrderView(generic.View):
    def get(self, request):
        form = OrderForm(request.user)
        return render(request, 'order/order.html', {'form': form})


    
    def post(self, request):
        form = OrderForm(request.POST)
        cart = Cart(request)
        if form.is_valid():
            order = form.save()     #мы уже создали заказ 
            for item in cart:
                OrderItem.objects.create(order=order, 
                                        product = item['product'],
                                        price = item['price'],
                                        quantity = item['quantity'])
            cart.clear()
            return render(request, 'order/order_created.html')
