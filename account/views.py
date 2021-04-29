from django.shortcuts import render
from .forms import RegistrationForm



def user_register(request):
    form = RegistrationForm()
    return  render(request, "account/register.html", {'form':form})


# после успешной регистрации пользователя надо перекинуть на страницу авторизацию

# Авторизаия
#-login.html
#-url
#-view