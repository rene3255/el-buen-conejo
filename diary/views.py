from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from diary.forms import AddActivityForm
from farms.models import ProducerProfile
from diary.models import Diary
# Create your views here.
@login_required(login_url='login')
def add_activity(request):
    if request.method == 'POST':
        form = AddActivityForm(request.POST, request.FILES)
        if form.is_valid():
            diary = form.save(commit=False)
            valid_producer = ProducerProfile.producers.get(id=request.user.id)
            if valid_producer:
                diary.farm_id = valid_producer.id
                if diary.costs is None:
                    diary.costs = "0.00"
                diary.is_active = True
                form.save()
                return redirect('home')
            
    else:
        form=AddActivityForm()
        
    return render(request,'Diary/AddActivity.html',
            {
            'form' : form,
            'error': form.errors
           
            }
    )

@login_required(login_url='login')   
def activities_list(request):
    diary = Diary.objects.register_active().filter(farm=request.user.id)
    print("Bitacora",diary)
    if not diary:
        print("Nothing")
        return redirect('home')
    print("There are to large diary")  
    context = {"diary": diary}
    return render(request, 'Diary/DiaryActivities.html', context )
  
    