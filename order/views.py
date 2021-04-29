from django.shortcuts import render
from django.views import generic
from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem

# Create your views here.
class OrderView(generic.View):
    def get(self, request):
        form = OrderForm(request.user)
        return render(request,'order/order.html',{'form':form})

    def post(self,requst):
        form = OrderForm(requst.user)
        cart = Cart(requst)
        if form.is_valid():
            order = form.save() #мы создали заказ
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price =item['price'],
                                         quantity = item['quantity'])
            cart.clear()
            return render(requst,'order/order_created.html')


