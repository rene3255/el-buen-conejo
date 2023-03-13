from django.urls import path
from doe.views import add_doe, does_list

urlpatterns = [
    path('add-doe/', add_doe,name='add-doe'),
    path('does-list/', does_list, name='does-list')
    
]