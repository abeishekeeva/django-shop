from django import forms 

PRODUCT_CHOICE_QUANTITY = [(i, str(i)) for i in range(1,21)]

class ProductAddForm(forms.Form):
    override = forms.BooleanField(required = False, initial = False, widget=forms.HiddenInput)
    quantity = forms.TypedChoiceField(choices=PRODUCT_CHOICE_QUANTITY, initial = 1)


