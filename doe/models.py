from django.db import models
from rabbit.models import Rabbit
from managers.managers import RecordManager
from cage.models import Cage
from farms.models import ProducerProfile
# Create your models here.

class ActiveDoeManager(models.Manager):
    def get_queryset(self):
        return super(ActiveDoeManager,
                  self).get_queryset().filter(is_active=True)
        
class Doe(models.Model):
    doe_name = models.CharField(max_length=50)
    selection_date = models.DateField(null=True, blank=True)
    doe_rabbit = models.ForeignKey(Rabbit, on_delete=models.CASCADE)
    farm = models.ForeignKey(ProducerProfile, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
          verbose_name = "Doe"
          verbose_name_plural = "Does"
          default_manager_name = "objects"
          
    def __str__(self) -> str:
        return self.doe_name
      
    objects = RecordManager()