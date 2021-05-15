from django import forms 

class CouponForm(forms.Form):
    coupon_code = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите код', }), label='')