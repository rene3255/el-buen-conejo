from django.urls import path

from . import views
urlpatterns = [
    path('add-doe/',views.add_doe,name='add-doe'),
    
]