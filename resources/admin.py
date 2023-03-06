from django.contrib import admin
from resources.models import State, City, Breed, RabbitStatus

admin.site.register(State)
admin.site.register(City)
admin.site.register(Breed)
admin.site.register(RabbitStatus)
