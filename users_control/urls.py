from django.urls import path, include

from . import views
urlpatterns = [
    path('register',views.register,name='register'),
    path('logout',views.elbuenconejo_logout,name='logout'),
    path('login', views.elbuenconejo_login,name='login'),
]
