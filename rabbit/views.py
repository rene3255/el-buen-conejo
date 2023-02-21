from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rabbit.models import Rabbit
from farms.models import ProducerProfile
# Create your views here.

@login_required(login_url='login')
def add_rabbit(request):
    valid_producer = ProducerProfile.producers.filter(id=request.user.id).first()
    if valid_producer:
        print("You are already to manage rabbits farm")
        context={'msg': 'You are already to manage rabbits farm'}
    else:
        context={'msg':'You have not authorized to manage rabbits'}
        return render(request,"Rabbit/AddRabbit.html",context)      
    return render(request,"Rabbit/AddRabbit.html",context)   
