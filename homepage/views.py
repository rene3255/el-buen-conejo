from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {
        'elbuenconejo': 'Hello from hompage view'
    }
    return render(request,'homepage/homepage.html',context)    

def login(request):
    context = {
        'elbuenconejo': 'Hello from hompage view'
    }
    return render(request,'Login/Login.html',context)

def register(request):
    context = {
        'elbuenconejo': 'Hello from hompage view'
    }
    return render(request,'Register/Register.html',context) 

def home(request):
    context = {
        'elbuenconejo': 'Hello from hompage view',
        'path_rute':'home'
    }
    return render(request,'home/home.html',context)     

def details(request):
    context = {
        'elbuenconejo': 'Hello from hompage view',
        'path_rute':'details'
    }
    return render(request,'MarketDetails/MarketDetails.html',context)   
  