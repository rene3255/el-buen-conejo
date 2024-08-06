from django.urls import path

from . import views

urlpatterns = [
    path(
        "producer-profile/<int:id>/myprofile",
        views.update_producer_profile,
        name="myprofile",
    ),
]
