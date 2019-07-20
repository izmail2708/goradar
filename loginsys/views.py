from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth 
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, UserRegistrationForm
from django.conf import settings
from django.core.mail import send_mail
from .decorators import check_recaptcha

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '').strip()
        password = request.POST.get('pass', '').strip()
        user = authenticate(username=username, password=password)
        if user is None:
            args['login_error']= 'Пользователь не найден'
            return render_to_response('loginsys/login.html', args)
        else:
            auth.login(request, user)
            return redirect('/')
    else:
        return render_to_response('loginsys/login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            if request.recaptcha_is_valid:
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                return render(request, 'loginsys/register_done.html', {'new_user': new_user, 'username': auth.get_user(request).username})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'loginsys/register.html', {'user_form': user_form})


