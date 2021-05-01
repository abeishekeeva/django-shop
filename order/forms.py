from .models import Order
from django import forms


class Order(forms.ModelForm):
    class Meta:
        model = Order
        fields = [ 'address', 'postal_code']