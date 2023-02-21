
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
      
    if request.method == 'GET':
        form=RegisterForm()
        return render(request,'Register/Register.html',{
            'form' : form,'error':''
        })
    

    form = RegisterForm( data=request.POST)
    if request.method == 'POST' and form.is_valid():

        user = form.save()
        if user:
            login(request,user)
            messages.success(request,'Cuenta creada exitosamente')
            return redirect('home')
    else:
        form=RegisterForm()
        return render(request,'Register/Register.html',{
            'form' : form,'error':'datos incorrectos'
        })      

def elbuenconejo_login(request):
    if request.user.is_authenticated:
        return redirect('home')
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

def elbuenconejo_logout(request):
    if not request.user.is_authenticated:
        return render(request,'homepage/homepage.html')
      
    if request.method == 'GET':
        logout(request)
    
    return render(request,'homepage/homepage.html')