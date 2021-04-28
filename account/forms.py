from django import forms 
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', }), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль повторно', }), label='')    

    class Meta:
        model = User 
        fields = ('email', )

    def clean_password2(self):
        cd = self.cleaned_data 
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2'] 

    