from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction


class CageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cage'
   
    def ready(self):
        from rabbit.models import Rabbit
        @receiver(post_save, sender=Rabbit)
        def update_rabbit_number(sender,instance, **kwargs):
            
            with transaction.atomic():
                from .models import Cage
                cage = Cage.objects.get(farm=instance.cage.farm, id=instance.cage_id)
                print('RABBITS_CAGE ',instance.cage_id)
                print('Farm: ',cage.farm)
                print('TITLE: ',cage.cage_title)
                cage.rabbits_number += 1
                cage.save()
        
        
         
          
