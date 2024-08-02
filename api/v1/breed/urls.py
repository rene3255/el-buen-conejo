from django.urls import path, include
from api.v1.breed.views import breed_list

urlpatterns = [
    path('breed-list/',breed_list,name='breed-list'),
    
]
