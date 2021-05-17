from django import forms

class CouponForm(forms.Form):
    coupon_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите код купона', }), label='')