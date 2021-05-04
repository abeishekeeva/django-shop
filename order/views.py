from django.shortcuts import render
from django.views import generic
from .forms import OrderForm
from cart.cart import Cart 
from .models import OrderItem
from django.contrib.auth.decorators import login_required

class OrderView(generic.View): 

    def get(self, request):
        form = OrderForm()
        return render(request, 'order/checkout.html', {'form': form})

    def post(self, request):
        form = OrderForm(request.POST)
        cart = Cart(request)
        if form.is_valid():
            order = form.save(commit=False)#мы уже создали заказ
            order.user = request.user #
            order.save() # заказ сахранен в базу данных
            for item in cart:                
                OrderItem.objects.create(order=order, 
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            cart.clear()
            return render(request, 'order/order_created.html')

        return render(request, 'order/checkout.html', {'form': form})





