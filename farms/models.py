from django.db import models
from users_control.models import CustomUser
from resources.models import State
from django.db.models.signals import post_save
# Create your models here.
class ProducerProfile(models.Model):
  
    first_name    = models.CharField(max_length=80, null=True, blank=True)
    last_name     = models.CharField(max_length=100, null=True, blank=True)
    state         = models.OneToOneField(State, on_delete=models.CASCADE, null=True, blank=True)
    photo         = models.ImageField('Producer profile',upload_to="farms/",
                                      null=True, blank=True)
    farm_name     = models.CharField(max_length=150, null=True, blank=True)
    address       = models.CharField(max_length=200, null=True, blank=True)
    producer      = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return f'Perfil del productor {self.producer}'
  
def create_profile(sender,instance,created,**kwargs):
    if created:
        ProducerProfile.objects.create(producer=instance)

post_save.connect(create_profile,sender=CustomUser)