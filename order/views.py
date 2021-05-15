from django.shortcuts import render
from django.views import generic 
from .forms import OrderForm
from cart.cart import Cart 
from .models import OrderItem
from django.views.generic import View
from django.contrib.auth.decorators import login_required 
from django.conf import settings
from django.contrib.auth.models import User
from .tasks import notify_user_on_order
from django.http import HttpResponse

def index(request):
    return HttpResponse('Done!')

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
            order.user = request.user  
            order.save()
            for item in cart:                
                OrderItem.objects.create(order=order, 
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])             
            cart.clear()
            notify_user_on_order.delay(order.id)
            return render(request, 'order/order_created.html')
        return render (request, 'order/checkout.html', {'form':form})





# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.views.generic.edit import FormView
# from django.shortcuts import redirect

# from .forms import GenerateRandomUserForm
# from .tasks import create_random_user_accounts

# class GenerateRandomUserView(FormView):
#     template_name = 'core/generate_random_users.html'
#     form_class = GenerateRandomUserForm

#     def form_valid(self, form):
#         total = form.cleaned_data.get('total')
#         create_random_user_accounts.delay(total)
#         messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
#         return redirect('users_list')



