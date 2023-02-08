
from django.shortcuts import render
from wsgiref.util import request_uri
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from users_control.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import  messages
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm
from django.views import generic
from django.contrib.auth import views as auth_views


# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():

        user = form.save()
        if user:
            login(request,user)
            messages.success(request,'Cuenta creada exitosamente')
            return redirect('home')
           

    return render(request,'users_control/register.html',{
        'form' : form,
    })

def elbuenconejo_login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'Login/Login.html',{
            'form' : form,'error':''
        })
    form = LoginForm(request=request, data=request.POST)
    
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
           login(request,user)
           return redirect('home')
        else:
            form = LoginForm()
            return render(request,'Login/Login.html',{
                'form' : form,'error':'datos incorrectos'
            })
    else:
        form = LoginForm()
        return render(request,'Login/Login.html',{
            'form' : form,'error':'datos incorrectos'
        })          
'''
class LoginView(auth_views.LoginView):
    template_name = 'users_control/login.html'
    form_class = LoginForm
'''

def elbuenconejo_logout(request):
    print(request)
    if not request.user.is_authenticated:
        
        return redirect('home')
    else: 
        print("Usuario", request.user.username)
        logout(request)
        messages.success(request,'Salió de sesión exitosamente')
        return redirect('home')
          