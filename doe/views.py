from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from doe.forms import AddDoeForm
from doe.models import Doe
from farms.models import ProducerProfile
from rabbit.models import Rabbit

# Create your views here.
@login_required(login_url='login')
def add_doe(request):
    if request.method == 'POST':
        form = AddDoeForm(request.POST, request.FILES)
      
        
        if form.is_valid():
            valid_producer = ProducerProfile.producers.get(id=request.user.id)
            if valid_producer:
               
                form.save()
                return redirect('home')
            
    else:
        form=AddDoeForm()
        
    return render(request,'Doe/AddDoeRabbit.html',
            {
            'form' : form,
            'error': form.errors
           
            }
    )      

@login_required(login_url='login')
def does_list(request):
    does = Doe.objects.register_active().filter()
    print(does)
    if not does:
        print("Nothing")
        return redirect('home')
    print("There are to many rabbits")  
    context = {"does": does}
    return render(request, 'doe/DoeList.html', context )
  
    
