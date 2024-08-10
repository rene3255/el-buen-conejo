from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cage.forms import AddCageForm
from cage.models import Cage
from rabbit.models import Rabbit
from django.db.models import Count, F, Value
from farms.models import ProducerProfile


# Create your views here.
@login_required(login_url="login")
def add_cage(request):

    if request.method == "POST":
        form = AddCageForm(request.POST, request.FILES)
        if form.is_valid():
            cage = form.save(commit=False)
            print("ID ACTIVO: ", request.user.id)
            try:
                valid_user = ProducerProfile.producers.get(id=request.user.id)
                if valid_user:
                    cage.farm = valid_user
                    cage.save()
                if cage:
                    return redirect("add-rabbit")
            except ProducerProfile.DoesNotExist:
                return render(
                    request,
                    "Cage/AddCage.html",
                    {"form": form, "error": "No eres productor"},
                )
    else:
        form = AddCageForm()
    return render(
        request,
        "Cage/AddCage.html",
        {"form": form, "error": "Inconsitencia en el llenado"},
    )


def cage_details(request, id):
    pass


def delete_cage(request, id):
    cage_founded = Cage.objects.get(id=id)
    try:
        cage_founded.delete()
    except:
        pass
    return redirect("cage-list")


def cages_list(request):
    rabbits_per_cage = (
        Cage.objects.filter(farm=request.user.id, is_active=True)
        .annotate(rabbit_count=Count("rabbit"))
        .values("cage_title", "rabbit_count")
    )
    return render(request, "Cage/CagesList.html", {"cages": rabbits_per_cage})
