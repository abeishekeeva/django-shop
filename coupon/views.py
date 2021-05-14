from django.shortcuts import render
<<<<<<< HEAD
from .models import Coupon
from. forms import CouponForm
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

# Create your views here.
@require_POST
def apply_coupon(request):
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iecxact=code,
                                        valid_form__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['coupon_id']=coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
=======

# Create your views here.
>>>>>>> origin
