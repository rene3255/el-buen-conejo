from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mating.forms import AddMatingForm
from doe.models import Doe
from buck.models import Buck
from farms.models import ProducerProfile
from mating.models import Mating

# Create your views here.
@login_required(login_url='login')
def add_mating(request):
    if request.method == 'POST':
        form = AddMatingForm(request.POST, request.FILES)
        print("Adding")
        if form.is_valid():
            
            valid_producer = ProducerProfile.producers.get(id=request.user.id)
            if valid_producer:
               
                mating = form.save(commit=False)    
                mating.farm =valid_producer
                form.save()
                return redirect('home')
            
    else:
        form=AddMatingForm()
        
    return render(request,'Mating/AddMating.html',
            {
            'form' : form,
            'error': form.errors
           
            }
    )      

@login_required(login_url='login')
def matings_list(request):
    matings = Mating.objects.filter(farm=request.user.id, is_active=True)
    print("HEMBRAS ", matings)
    if not matings:
        print("Nothing")
        return redirect('home')
    print("There are to many rabbits")  
    context = {"matings": matings}
    return render(request, 'Mating/MatingsList.html', context )
  
    
