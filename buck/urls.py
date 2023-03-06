from django.urls import path
from buck.views import add_buck
from . import views
urlpatterns = [
    path('add-buck/',add_buck,name='add-buck'),
    
]