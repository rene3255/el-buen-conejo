from django.urls import path, include

from . import views
app_name = 'users_control'
urlpatterns = [
    path('register',views.register,name='register'),
    path('logout',views.elbuenconejo_logout,name='logout'),
    path('login', views.LoginView.as_view(
              template_name='users_control/login.html',
              redirect_authenticated_user=True), name='login'),
]
