from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('', include('users_control.urls')),
    path('', include('farms.urls')),
    path('', include('cage.urls')),
    path('', include('rabbit.urls')),
    path('', include('doe.urls')),
    path('', include('buck.urls')),
    path('', include('diary.urls')),
    path('', include('mating.urls')),
    path('api/v1/breed/', include('api.v1.breed.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

