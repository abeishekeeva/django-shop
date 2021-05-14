from django.shortcuts import render
from django.views import generic
from .forms import OrderForm
from cart.cart import Cart 
from .models import OrderItem
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .tasks import notify_user_on_order

class OrderView(generic.View): 

    def get(self, request):
        form = OrderForm()
        return render(request, 'order/checkout.html', {'form': form})
    # @login_required(login_url='/login/')
    def post(self, request):
        form = OrderForm(request.POST)
        cart = Cart(request)
        if form.is_valid():
            order = form.save(commit=False) #мы уже создали заказ
            order.user = request.user  #Anonymous User 
            order.save()
            for item in cart:                
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])             
            cart.clear()
            notify_user_on_order.delay(order.id)
            return render(request, 'order/order_created.html')

        return render(request, 'order/checkout.html', {'form': form})



