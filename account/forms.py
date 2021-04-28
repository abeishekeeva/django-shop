from django import forms 
from django.contrib.auth.models import User



class LoginForm(forms.Form): 
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите свой email',}), label = '')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите свой пароль',}), label = '')
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        return self.cleaned_data 


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Введите email',}), label = '')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите свой пароль',}), label = '')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль повторно',}), label = '')
    class Meta: 
        model = User 
        fields = ('email',)
    
    def clean_password2(self):
        cd = self.cleaned_data 
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Ваши пароли не совпадают')
        return cd['password2'] 


