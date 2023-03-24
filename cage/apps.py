from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver


class CageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cage'
   
    def ready(self):
        from rabbit.models import Rabbit
        @receiver(post_save, sender=Rabbit)
        def update_rabbit_number(sender,instance, **kwargs):
            from .models import Cage
            cage = Cage.objects.get(id=instance.cage.id)
            num_rabbits = cage.rabbits_number
            cage.rabbits_number = num_rabbits + 1
            num_rabbits = 0
            cage.save()
        
        
         
          
