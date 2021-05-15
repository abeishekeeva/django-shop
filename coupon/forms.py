from django import forms 
from .models import Coupon

class CouponForm(forms.Form):       
    coupon_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите купон', }), label='')
