from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mating.forms import AddMatingForm
from doe.models import Doe
from buck.models import Buck
from farms.models import ProducerProfile
from mating.models import Mating
from datetime import date, timedelta

# Create your views here.
@login_required(login_url='login')
def add_mating(request):
    if request.method == 'POST':
        form = AddMatingForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            valid_producer = ProducerProfile.producers.get(id=request.user.id)
            if valid_producer:
                mating = form.save(commit=False)   
                valid_mating_date = ValidMatingDate(mating,request.user.id)
                if valid_mating_date.is_valid_mating():
                    mating.farm =valid_producer
                    form.save()
                    return redirect('home')
                else:
                    form.add_error("mating_date","Mating already exists")
                    
    else:
        form=AddMatingForm(request=request)
        
    return render(request,'Mating/AddMating.html',
            {
            'form' : form,
            'error': form.errors
           
            }
    )      

@login_required(login_url='login')
def matings_list(request):
    matings = Mating.objects.filter(farm=request.user.id, is_active=True)
    if not matings:
        return redirect('home')
    context = {"matings": matings}
    return render(request, 'Mating/MatingsList.html', context )
  
    
class ValidMatingDate:
    def __init__(self, mating_form,
                    user):
        
        self.mating_form = mating_form
        self.user = user
        self.fetch_mating = Mating.objects.filter(doe=self.mating_form.doe_id, mating_succeeded=True, farm=user, is_active=True).first()
       
        
    @property
    def is_valid_entered_date(self):
        
        return self.mating_form.mating_date <= date.today()
       
    @property
    def is_mating_forbidden(self): 
        return self.fetch_mating.mating_date \
                + timedelta(days=50) >= self.mating_form.mating_date if not self.fetch_mating==None else False
          
      
    def is_valid_mating(self):
        return self.is_valid_entered_date and (not self.is_mating_forbidden)
          
            
                    
              
          
      
          
          