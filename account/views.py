from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.messages import constants as messages
# Create your views here.

class UserRegisterView(generic.View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'account/register.html', {'form': form})
    def post(self, request):       
        form = UserRegistrationForm(request.POST)
        #cd = form.cleaned_data 
        user_exists = User.objects.filter(email=request.POST['email']).exists()
        if not user_exists: 
            if form.is_valid(): 
                new_user = form.save(commit=False)
                new_user.username = request.POST['email']
                new_user.set_password(form.cleaned_data['password1'])
                new_user.save()                
                return redirect('') #редирект на логин
            else:
               messages.error(request, 'Неправильные данные') 
        else:
            messages.error(request, 'Такой пользователь уже есть')
        return render(request, 'account/register.html', {'form': form})


class LoginView(generic.View):
    
    def get(self, request):
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('') #сюда вставить, куда редиректить
                else:
                    messages.error(request, 'Ваш аккаунт заблокирован')
            else:
                messages.error(request, 'Неправильный ввод данных')
        return render(request, 'account/login.html', {'form': form})        
