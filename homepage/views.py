from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from farms.models import ProducerProfile
from django.shortcuts import redirect

# Create your views here.


def homepage(request):
    context = {"elbuenconejo": "Hello from hompage view"}
    return render(request, "homepage/homepage.html", context)


@login_required
def home(request):
    context = {"elbuenconejo": "Hello from hompage view", "path_rute": "home"}
    return render(request, "home/home.html", context)


@login_required
def details(request):
    context = {"elbuenconejo": "Hello from hompage view", "path_rute": "details"}
    return render(request, "MarketDetails/MarketDetails.html", context)


@login_required
def profile(request):
    context = {"elbuenconejo": "Hello from hompage view", "path_rute": "details"}
    return render(request, "Profile/Profile.html", context)


@login_required
def myprofile(request):
    try:
        producer_profile = ProducerProfile.producers.get(id=request.user.id)

        return render(
            request, "myProfile/MyProfile.html", {"producer_profile": producer_profile}
        )
    except ProducerProfile.DoesNotExist:
        return redirect("homepage")
