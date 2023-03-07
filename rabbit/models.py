from django.db import models
from django.utils.functional import cached_property
from resources.models import Breed, RabbitStatus
from cage.models import Cage
# Create your models here.

class ActiveRabbitManager(models.Manager):
    def get_queryset(self):
        return super(ActiveRabbitManager,
                  self).get_queryset().filter(is_active=True)

class MaleRabbitManager(models.Manager):
    def get_queryset(self):
        return super(ActiveRabbitManager,
                  self).get_queryset().filter(male='M', is_active=True)
    
   
class Rabbit(models.Model):
    
    RABBIT_ACTIVE = (
      (True, 'Si'),
      (False,'No'),
    )
    
    RABBIT_SEX = (
      ('M','Macho'),
      ('H','Hembra'),
    )
    
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    sex   = models.CharField(max_length=1, 
                            choices=RABBIT_SEX, default=RABBIT_SEX[0][1])
    rabbit_tag = models.CharField(max_length=30, 
                        null=True, blank=True, unique=True
                        )
    birth_date = models.DateField(null=True, blank=True)
    weight = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    rabbit_photo = models.ImageField('Foto del conejo',upload_to="media/rabbits/", default="rabbit_avatar.png",
                                      null=True, blank=True)   
    rabbit_status = models.ForeignKey(RabbitStatus,on_delete=models.CASCADE)
    observation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    cage = models.ForeignKey(Cage, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    objects = models.Manager()
    active_rabbit = ActiveRabbitManager()
    male_rabbit = MaleRabbitManager()
    
    class Meta:
          verbose_name = "Rabbit"
          verbose_name_plural = "Rabbits"
          default_manager_name = "objects"
          
          
  
  
            
    
    def __str__(self):
      
        if self.sex == "M":
            complete_sex = "Male"
        if self.sex == "H":
            complete_sex = "Female"
                        
        result = self.rabbit_tag + \
               " " + str(self.rabbit_status) + \
               "\n" + complete_sex
        return result           
      
    @cached_property
    def rabbit_name(self):
        return self.rabbit_tag + " " + self.sex
