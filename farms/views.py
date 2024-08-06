from django.shortcuts import render, redirect
from farms.forms import ProfileForm
from farms.models import ProducerProfile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="login")
def update_producer_profile(request, id):
    producer_data = ProducerProfile.objects.get(id=id)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=producer_data)
        if form.is_valid():
            producer_profile = form.save(commit=False)
            producer_profile.is_producer = True
            producer_profile.save()
            if producer_profile:
                return redirect("home")
    else:
        form = ProfileForm(instance=producer_data)
    return render(request, "Producer/Producer.html", {"form": form})
