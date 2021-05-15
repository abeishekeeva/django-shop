from django.shortcuts import render 
from django.views.decorators.http import require_POST
from .forms import CouponForm
from django.utils import timezone



@require_POST
def apply_coupon(request):
    now=timezone.now()
    form = CouponForm(request.POST)
    
    if form.is_valid(): 
        coupon_code = form.cleaned_data['coupon_code']
    try:
        code=objects.get[coupon_code]
       

# '''@require_POST
# def coupon_apply(request):
#  now = timezone.now()
#  form = CouponApplyForm(request.POST)
#  if form.is_valid():
#  code = form.cleaned_data['code']
#  try:
#  coupon = Coupon.objects.get(code__iexact=code,
#  valid_from__lte=now,
#  valid_to__gte=now,
#  active=True)
#  request.session['coupon_id'] = coupon.id
#  except Coupon.DoesNotExist:
#  request.session['coupon_id'] = None
#  return redirect('cart:cart_detail')'''