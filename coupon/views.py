from django.shortcuts import render
from .forms import CouponForm
from django.views.decorators.http import require_GET, require_POST

@require_POST
def apply_coupon(request): 
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid:
        cd = form.cleaned_data['coupon_code']
        try:
            coupon = Coupon.objects.get(code__iexact = code,
                                        valid_from__lte = now,
                                        valid_to_gte = now,
                                        active = True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
             

