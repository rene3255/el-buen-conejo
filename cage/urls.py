from django.urls import path, include

from . import views
urlpatterns = [
    path('add-cage/',views.add_cage,name='add-cage'),
    path('delete-cage/<int:id>',views.delete_cage,name='delete-cage'),
    path('cage-details/<int:id>', views.cage_details,name='cage-details'),
    path('cages-list/', views.cages_list,name='cages-list'),
    
]