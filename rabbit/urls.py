from django.urls import path

from rabbit.views import add_rabbit
urlpatterns = [
    path('add-rabbit/',add_rabbit,name='add-rabbit'),
    
]