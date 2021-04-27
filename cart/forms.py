from django import forms 

<<<<<<< HEAD
PRODUCT_CHOICE_QUANTITY = [(i, str(i)) for i in range(1,21)]

class ProductAddForm(forms.Form):
    override = forms.BooleanField(required = False, initial = False, widget=forms.HiddenInput)
    quantity = forms.TypedChoiceField(choices=PRODUCT_CHOICE_QUANTITY, initial = 1)


=======
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class ProductAddForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
>>>>>>> 1cd8cb2885fa20310957184f0f67ba12858b7678
