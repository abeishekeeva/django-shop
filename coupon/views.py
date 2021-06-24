# from django.shortcuts import render
# from .forms import CouponForm
# from django.views.decorators.http import require_GET, require_POST

# @require_POST
# def apply_coupon(request): 
#     now = timezone.now()
#     form = CouponForm(request.POST)
#     if form.is_valid():
#         code = form.cleaned_data['coupon_code']
#         try:
#             coupon = Coupon.objects.get(code=code, active=True)
#             request.session['coupon_id'] = coupon.id
#             print(request.session['coupon_id'])
#         except Coupon.DoesNotExist:
#             request.session['coupon_id'] = None
#     return redirect('card:cart_detail')
                


# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Coupon
from .forms import CouponForm


@require_POST
def apply_coupon(request):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['coupon_code']
        try:
            coupon = Coupon.objects.get(code=code, active=True)
            request.session['coupon_id'] = coupon.id
            print(request.session['coupon_id'])
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('card:cart_detail')
                

