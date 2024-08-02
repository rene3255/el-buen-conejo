from django.urls import path, include

from . import views

urlpatterns = [
    path(
        "producer-profile/<int:id>/",
        views.update_producer_profile,
        name="producer-profile",
    ),
]
