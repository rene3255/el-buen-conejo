from django.urls import path

from rabbit.views import add_rabbit, rabbits_list
urlpatterns = [
    path('add-rabbit/',add_rabbit,name='add-rabbit'),
    path('rabbits-list/',rabbits_list,name='rabbits-list'),
    
]