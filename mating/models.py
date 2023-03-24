from django.db import models
from buck.models import Buck
from doe.models import Doe
# Create your models here.
class Mating(models.Model):
  
    class Stars(models.IntegerChoices):
        NINGUNA = 0, "NINGUNA"
        UNA = 1, "UNA"
        DOS = 2, "DOS"
        TRES = 3, "TRES"
        CUATRO = 4, "CUATRO"
        CINCO = 5, "CINCO"
        
    buck = models.ForeignKey(Buck, on_delete=models.CASCADE)
    doe = models.ForeignKey(Doe, on_delete=models.CASCADE)
    comments = models.TextField(blank=True, default='')
    vote = models.IntegerField(choices=Stars.choices, 
                               default=Stars.NINGUNA,
                               verbose_name = "stars")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
                                      
                                      