from django.db import models
from farms.models import ProducerProfile
from django.utils.functional import cached_property
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class CageManager(models.Manager):
    def cage_title_count(self,keyword):
        return self.filter(cage_title__icontains=keyword).count()
    
    def list_cages(self):
        return self.filter(cage_title__isnull=False)
    
    def cages_by_farm(self, farm):
        return self.filter(cage_title__isnull=False, farm=farm) 
      

class PublicCageManager(models.Manager):
    def get_queryset(self):
        return super(PublicCageManager,
                     self).get_queryset().filter(is_public=True)

class PrivateCageManager(models.Manager):
    def get_queryset(self):
        return super(PrivateCageManager,
                     self).get_queryset().filter(is_public=False)

                  
class Cage(models.Model):
    CAGE_PUBLIC = (
      (True, 'Si'),
      (False, 'No'),
    )
    
    cage_title = models.CharField(max_length=50, unique=True)
    is_public = models.BooleanField(choices=CAGE_PUBLIC, 
                                 default=CAGE_PUBLIC[1][0])
    details = models.CharField(max_length=255,null=True, blank=True)
    cage_photo =  models.ImageField('Producer profile',upload_to="media/cage",
                                    default="cage_avatar.png",
                                      null=True, blank=True)   
                # upload_to="media/rabbits/", default="rabbit_avatar.png",
                #                      null=True, blank=True)
    farm = models.ForeignKey(ProducerProfile, on_delete=models.CASCADE, related_name="cages")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    cages = CageManager()
    public_cages = PublicCageManager()
    private_cages = PrivateCageManager() 
    
    
    
      
    class Meta:
        verbose_name = "Lista de Jaulas"
        verbose_name_plural = "Total de Jaulas"
        default_manager_name = "objects"
        
                
    def __str__(self):
        if self.is_public:
            publish = " es pública"
        else:
            publish = " no es pública"
        return "Jaula " + self.cage_title + publish
      
    @cached_property
    def rabbits_per_cage(self):
        return self.cage_title + " " + self.rabbits_number 
    