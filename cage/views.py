from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from cage.forms import AddCageForm
from cage.models import Cage
from django.db.models import Count, F, Value
from farms.models import ProducerProfile
import os
from django.conf import settings
from PIL import Image
# Create your views here.
@login_required
def add_cage(request):
    
    if request.method == 'POST':
        form = AddCageForm(request.POST, request.FILES)
        if form.is_valid():
            cage = form.save(commit=False)
            print("request.user ",request.user.id)
            producer_id = ProducerProfile.objects.producer_valided(request.user.id)
            #producer_id = ProducerProfile.objects.filter(id=request.user.id, first_name__isnull=False).first()
            cage.farm =producer_id
            cage.is_producer = True
            cage.save()
            if cage:
                return redirect('home')
    else:
        form=AddCageForm()
    return render(request,'Cage/AddCage.html',{
            'form' : form, 'error':'Inconsitencia en el llenado'
        })      

def cage_details(request,id):
    pass

def delete_cage(request,id):
    cage_founded = Cage.objects.get(id=id)
    try:
        cage_founded.delete()
    except:
        pass
    return redirect('cage-list')
  
def cages_list(request):
    print("user activo: %s" % request.user.id)
    cage_resultset = Cage.cages.list_cages().filter(farm=request.user.id)
    return render(request,
                  "Cage/CagesList.html",
                  {'cages':cage_resultset})
   