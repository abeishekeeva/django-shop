from django import forms
from .models import Order 

class OrderForm(forms.Form):    
    class Meta:
        model = Order 
        fields = ['user', 'address', 'postal_code']


