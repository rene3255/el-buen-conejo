from django.db import models
from users_control.models import CustomUser
from resources.models import City
from django.db.models.signals import post_save
# Create your models here.

class ProducerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_producer=True)


class ProducerProfile(models.Model):
  
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField('Producer profile',upload_to="media/",
                                      null=True, blank=True)
    farm_name = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    is_producer = models.BooleanField(default=False)
    producer = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    objects = models.Manager()
    producers = ProducerManager()
    
    def __str__(self):
        return f'Perfil del productor {self.producer}'
  
def create_profile(sender, instance, created,  **kwargs):
    if created:
        ProducerProfile.objects.create(producer=instance)

post_save.connect(create_profile,sender=CustomUser)
