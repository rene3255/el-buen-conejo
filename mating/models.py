from django.db import models
from buck.models import Buck
from doe.models import Doe
from farms.models import ProducerProfile
from datetime import date, timedelta
# Create your models here.
class Mating(models.Model):
        
    buck = models.ForeignKey(Buck, on_delete=models.CASCADE)
    doe = models.ForeignKey(Doe, on_delete=models.CASCADE)
    mating_date = models.DateField()
    observations = models.TextField(max_length=255)
    mating_succeeded = models.BooleanField(default=False)
    farm = models.ForeignKey(ProducerProfile, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property 
    def mating_approved(self):
        date_valid = ""
        if self.mating_succeeded:
          date_valid = self.mating_date + timedelta(days=50)
        return date_valid 
       
    class Meta:
      verbose_name = "Mating"
      verbose_name_plural = "Matings"
    
    def __str__(self):
        return str(self.buck) + " & " + str(self.doe)
                                      