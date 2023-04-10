from django.db import models
from rabbit.models import Rabbit
from farms.models import ProducerProfile
from managers.managers import RecordManager
# Create your models here.
class Buck(models.Model):
    buck_name = models.CharField(max_length=50)
    selection_date = models.DateField(null=True, blank=True)
    buck_rabbit = models.ForeignKey(Rabbit, on_delete=models.CASCADE)
    farm = models.ForeignKey(ProducerProfile, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
          verbose_name = "Buck"
          verbose_name_plural = "Bucks"
          default_manager_name = "objects"
          
    def __str__(self) -> str:
        return self.buck_name
      
    objects = RecordManager()