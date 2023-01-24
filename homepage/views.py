from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'elbuenconejo': 'Hello from hompage view'}
    return render(request,'homepage/homepage.html',context)    
  