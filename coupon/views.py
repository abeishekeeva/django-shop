from django.shortcuts import render, redirect
from .forms import CouponForm
from .models import Coupon
from django.utils import timezone
from django.views.decorators.http import require_POST

@require_POST
def apply_coupon(request):
    form = CouponForm(request.POST)
    #now = timezone.now()
    if form.is_valid(): 
        code = form.cleaned_data['coupon_code'] 
        try: 
            coupon = Coupon.objects.get(code=code, active=True) 
            request.session['coupon_id'] = coupon.id 
            print(f"COUPON ID {request.session['coupon_id']}")
        except Coupon.DoesNotExist: 
            request.session['coupon_id'] = None 
    return redirect('cart:cart_detail')

