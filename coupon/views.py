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
def coupon_apply(request):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['coupon_code']
        try:
<<<<<<< HEAD
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['coupon_id'] = coupon.id
            print(request.session['coupon_id'])
        except Coupon.DoesNotExists:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
=======
            coupon = Coupon.objects.get(code=code, active=True)
            request.session['coupon_id'] = coupon.id
            print(request.session['coupon_id'])
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('card:cart_detail')
                


>>>>>>> cfa0927... addint changes to coupon
