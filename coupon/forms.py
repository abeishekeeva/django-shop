from django import forms 
from .models import Coupon

class CouponForm(forms.Form):       
    coupon_code = forms.CharField()