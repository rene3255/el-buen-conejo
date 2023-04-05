from django.db import models
from django.utils.functional import cached_property
from resources.models import Breed, RabbitStatus
from cage.models import Cage
from farms.models import ProducerProfile


# Create your models here.

class ActiveRabbitManager(models.Manager):
    def get_queryset(self):
        return super(ActiveRabbitManager,
                  self).get_queryset().filter(is_active=True)

class MaleRabbitManager(models.Manager):
    def get_queryset(self):
        return super(MaleRabbitManager,
                  self).get_queryset().filter(male='M', is_active=True)
    
class DoeRabbitManager(models.Manager):
    def get_queryset(self):
        return super(DoeRabbitManager,
                  self).get_queryset().filter(rabbit_status__status='Doe', is_active=True, is_doe=False)

class BuckRabbitManager(models.Manager):
    def get_queryset(self):
        return super(BuckRabbitManager,
                  self).get_queryset().filter(rabbit_status__status='Buck', is_active=True, is_buck=False)
        
      
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
    birth_date = models.DateField(null=True, blank=True)
    rabbit_photo = models.ImageField('Foto del conejo',upload_to="media/rabbits/", default="rabbit_avatar.png",
                                      null=True, blank=True)   
    rabbit_status = models.ForeignKey(RabbitStatus,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    cage = models.ForeignKey(Cage, on_delete=models.CASCADE)
    farm = models.ForeignKey(ProducerProfile, on_delete=models.CASCADE)
    is_doe = models.BooleanField(default=False)
    is_buck = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    active_rabbit = ActiveRabbitManager()
    male_rabbit = MaleRabbitManager()
    fetch_doe_rabbits = DoeRabbitManager()
    fetch_buck_rabbits = BuckRabbitManager()
    
    
    def formatted_id_number(self,number):
        number_length = len(str(number))
        my_number = list(str(number))
        my_new_list = ['0','0','0']

        if number_length ==1:
            my_new_list[2] = my_number[0]
            
        if number_length == 2:
            my_new_list[2] = my_number[1]
            my_new_list[1] = my_number[0]
        if number_length == 3:
            my_new_list[0] = my_number[0]
            my_new_list[1] = my_number[1]
            my_new_list[2] = my_number[2]
            
        result = "".join(my_new_list) 
        
        return result

    @property
    def rabbit_tag(self):
        str_tag=''
        for char in self.farm.farm_name:
            if  char != ' ':
                str_tag += ''.join(char) 
        return f"{str_tag[:4]}-{self.formatted_id_number(self.id)}"
      

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
      
    
      