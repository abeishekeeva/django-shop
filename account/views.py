from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def user_register(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
    else:
        form = UserRegistrationForm(request.POST)
        #cd = form.cleaned_data
        user_exists = User.objects.filter(email=request.POST['email']).exists()
        if not user_exists:
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.username = request.POST['email']
                new_user.set_password(form.cleaned_data['password1'])
                new_user.save()

                return HttpResponseRedirect('/account/login/')
            else:
               messages.error(request, 'Неправильные данные')
        else:
            messages.error(request, 'Такой пользователь уже есть')

    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data #{'username': 'aidai', ;}
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request, 'Ваш аккаунт заблокирован')
            else:
                messages.error(request, 'Неправильный ввод данных')

    return render(request, 'account/login.html', {'login_form': form})
