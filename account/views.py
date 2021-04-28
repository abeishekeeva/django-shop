from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth.models import User 

# Create your views here.
 
# def user_register(request):
#     form = UserRegistrationForm()
#     return render(request, 'account/register.html', {'form': form})


def user_register(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
    else: 
        form = UserRegistrationForm(request.POST)
        # cd = form.cleaned_data 
        user_exists = User.objects.filter(email=request.POST['email']).exists()
        if not user_exists: 
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.username = request.POST['email']
                new_user.set_password(form.cleaned_data['password1'])
                new_user.save()
                User.objects.create(user = new_user, first_name='', last_name='')
                return HttpResponseRedirect('/login/')
            else:
                messages.error(request, 'Неправильные данные!')
        else: 
            messages.error(request, 'Такой пользователь уже есть!')
    
    return render(request, 'account/register.html', {'form': form})
