
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
  
class Profile(models.Model):
  
    USER_ROLES = (
        (1,'Productor'),
        (2,'Cliente'),
        (3,'Guest')
    )
  

    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name =  models.CharField(max_length=150, null=True, blank=True)
    email = models.mailField(max_length=254)
    state = models.OneToOneField(State, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile"
        plural_name = "Profiles"
        
    def __str__(self):
        return f'Perfil del {self.first_name}'
  
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile,sender=User)
