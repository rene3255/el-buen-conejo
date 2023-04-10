from django.db import models
from django.utils.functional import cached_property
from resources.models import Breed, RabbitStatus
from cage.models import Cage
from farms.models import ProducerProfile
import datetime

# Create your models here.

class RabbitTagTemplate:
    def __init__(self, 
                 farm_name, 
                 model_id, model_id_length=3):
        self.farm_name = farm_name,
        self.model_id = model_id
        self.model_id_length = model_id_length
        
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

        if number_length == 1:
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
        rabbit_tag = RabbitTagTemplate(self.farm.farm_name,3)
       # str_tag=''
       # for char in self.farm.farm_name:
       #     if  char != ' ':
       #         str_tag += ''.join(char) 
        return rabbit_tag.build_rabbit_tag() # f"{str_tag[:4]}-{self.formatted_id_number(self.id)}"
      

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

class RabbitTagTemplate:
    
    def __init__(self, 
                 farm_name, 
                 model_id, model_id_length=3, character_type="0"):
        self.farm_name = farm_name,
        self.model_id = model_id
        self.model_id_length = model_id_length
        self.character_type = character_type
        
        self.today = datetime.date.today()
        self.month = str(self.today.month)
    
    @property
    def model_id_template(self):
        pattern = self.character_type * self.model_id_length
        model_id_plus_pattern = pattern + str(self.model_id)
        pattern = model_id_plus_pattern[len(str(self.model_id)):len(model_id_plus_pattern)]
        return pattern
      
    @property
    def get_current_year(self):
        return str(self.today.year)[2:4]
      
    @property
    def get_current_month(self):
        month_template = "0"+self.month if len(self.month) == 1 else self.month
        return month_template
      
    @property
    def farm_name_pattern(self):
        farm = "".join(self.farm_name).upper()
        farm_one = farm[:self.model_id_length]
        farm_two = farm[-1]
        if " " in farm:
            pat = "".join("".join(farm).split())
            pattern_one = pat[:self.model_id_length]
            pattern_two = pat[-1]
            return pattern_one + pattern_two
        return farm_one + farm_two
        
    def build_rabbit_tag(self):
        builded_tag = self.farm_name_pattern + \
                      "-" + \
                      self.get_current_year + \
                      self.get_current_month + \
                      self.model_id_template
                      
        return builded_tag
      
      
    
      