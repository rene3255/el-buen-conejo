from django.urls import path
from buck.views import add_buck, bucks_list
from . import views
urlpatterns = [
    path('add-buck/', add_buck,name='add-buck'),
    path('bucks-list/', bucks_list, name='bucks-list')
    
]

