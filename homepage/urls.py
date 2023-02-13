from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home', views.home, name='home'),
    path('homepage', views.homepage, name='homepage'),
    path('makeDetails', views.details, name='makeDetails'),
    path('profile', views.profile, name='profile'),
]