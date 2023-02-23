from django.db import models
from resources.models import Breed, RabbitStatus
from cage.models import Cage
# Create your models here.
class Buck(models.Model):
    buck_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

class Doe(models.Model):
    Doe_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)


class Rabbit(models.Model):
    RABBIT_SEX = (
      ('H','Hembra'),
      ('M','Macho'),
    )
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    sex   = models.CharField(max_length=1, 
                            choices=RABBIT_SEX, default=RABBIT_SEX[1][0])
    rabbit_tag = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    father = models.ForeignKey(Buck, on_delete=models.CASCADE, null=True, blank=True)
    mother = models.ForeignKey(Doe, on_delete=models.CASCADE, null=True, blank=True)
    rabbit_photo = models.ImageField('Foto del conejo',upload_to="media/rabbits",
                                      null=True, blank=True)   
    rabbit_status = models.ForeignKey(RabbitStatus,on_delete=models.CASCADE)
    observation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    cage = models.ForeignKey(Cage, on_delete=models.CASCADE)
    
    class Meta:
          verbose_name = "Rabbit"
          verbose_name_plural = "Rabbits"

    def __str__(self):
        return self.rabbit_tag + \
               " " + self.rabbit_status + \
               "\n" + self.sex

    
    
    