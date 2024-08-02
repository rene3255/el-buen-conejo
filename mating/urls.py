from django.urls import path
from mating.views import add_mating, matings_list

urlpatterns = [
    path('add-mating/', add_mating,name='add-mating'),
    path('matings-list/', matings_list, name='matings-list')    
]