from django import forms 
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta: 
        model = Order
        fields = ['user', 'address', 'postal_code']