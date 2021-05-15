from django import forms
from .models import Order 

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order 
        fields = ['address', 'postal_code', 'country', 'city']




