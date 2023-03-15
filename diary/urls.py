from django.urls import path
from diary.views import add_activity, activities_list
urlpatterns = [
    path('add-activity/', add_activity,name='add-activity'),
    path('activities-list/', activities_list, name='activities-list'),
    
]