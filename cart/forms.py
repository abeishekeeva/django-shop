from django import forms

PRODUCT_CHOICE_QUANTITY = [i for i in range(1, 21)]

class ProductAddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices= PRODUCT_CHOICE_QUANTITY, initial=1)
    override = forms.BooleonField(required=False, initial = False, widget = forms.HiddenInput)
