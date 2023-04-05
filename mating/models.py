from django.db import models
from buck.models import Buck
from doe.models import Doe
# Create your models here.
class Mating(models.Model):
        
    buck = models.ForeignKey(Buck, on_delete=models.CASCADE)
    doe = models.ForeignKey(Doe, on_delete=models.CASCADE)
    comments = models.TextField(blank=True, default='')
    mating_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
                                      
                                      