from django.shortcuts import render,redirect, reverse
from django.contrib.auth.decorators import login_required
from diary.forms import AddActivityForm
from farms.models import ProducerProfile
from diary.models import Diary
# Create your views here.
@login_required(login_url='login')
def add_activity(request):
    context = {}
    last_activity_entered = {"activity": None }
    if request.method == 'POST':
        form = AddActivityForm(request.POST, request.FILES)
        if form.is_valid():
            
            diary = form.save(commit=False)
            valid_producer = ProducerProfile.producers.get(id=request.user.id)
            if valid_producer:
                context= {'my_activity': diary.activity }
                print("LAST ACT:", diary.activity )
                diary.farm_id = valid_producer.id
                if diary.costs is None:
                    diary.costs = "0.00"
                diary.is_active = True
                url = reverse('add-activity')+ '?my_activity={}'.format(context['my_activity'])
                form.save()
                return redirect(url)
            
    else:
        form=AddActivityForm()
        
    return render(request,'Diary/AddActivity.html',
            {
            'form' : form,
            'error': form.errors,
            'last_activity': last_five_activities(request.user.id)
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

def last_five_activities(my_user):
    diary = Diary.objects.register_active().filter(farm=my_user).order_by('-id')[:5]
    return diary  
    