from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rabbit.models import Rabbit
from farms.models import ProducerProfile
from rabbit.forms import AddRabbitForm
from cage.models import Cage
# Create your views here.

@login_required(login_url='login')
def add_rabbit(request):
    if request.method == 'POST':
        form = AddRabbitForm(request.POST, request.FILES,request=request)
        
        if form.is_valid():
            valid_producer = ProducerProfile.producers.get(id=request.user.id)
            if valid_producer:
                form.save()
                return redirect('home')
            
    else:
        user_id = ProducerProfile.objects.get(producer=request.user.id)
        form=AddRabbitForm(request=request)
        
    return render(request,'Rabbit/AddRabbit.html',
            {
            'form' : form,
            'error': form.errors
           
            }
    )      

@login_required(login_url='login')
def rabbits_list(request):
    rabbits = Rabbit.active_rabbit.filter(cage__farm=request.user.id)
    if not rabbits:
        return redirect('home')
        
    context = {"rabbits": rabbits}
    return render(request, 'rabbit/RabbitList.html', context )
  
    
    