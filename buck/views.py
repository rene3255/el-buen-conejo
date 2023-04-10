from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from buck.forms import AddBuckForm
from buck.models import Buck
from farms.models import ProducerProfile
from rabbit.models import Rabbit

# Create your views here.
@login_required(login_url='login')
def add_buck(request):
    if request.method == 'POST':
        form = AddBuckForm(request.POST, request.FILES)
      
        if form.is_valid():
            valid_producer = ProducerProfile.producers.get(id=request.user.id)
            
            if valid_producer:
                buck= form.save(commit=False)
                buck.farm = valid_producer
                form.save()
                return redirect('home')
            
    else:
        form=AddBuckForm()
        
    return render(request,'Buck/AddBuckRabbit.html',
            {
            'form' : form,
            'error': form.errors
           
            }
    )      

@login_required(login_url='login')
def bucks_list(request):
    bucks = Buck.objects.register_active().filter(buck_rabbit__cage__farm=request.user.id)
    
    if not bucks:
        return redirect('home')
    context = {"bucks": bucks}
    return render(request, 'Buck/BucksList.html', context)
  
    
