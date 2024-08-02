from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver




class RabbitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rabbit'

    def ready(self):
        from rabbit.models import Rabbit
        from doe.models import Doe
        
        @receiver(post_save, sender=Doe)
        def update_is_doe(sender,instance, **kwargs):
            rabbit = Rabbit.objects.get(id=instance.doe_rabbit_id)
            rabbit.is_doe = True
            rabbit.save()
            
        from buck.models import Buck
        @receiver(post_save, sender=Buck)
        def update_is_buck(sender,instance, **kwargs):
            rabbit = Rabbit.objects.get(id=instance.buck_rabbit_id)
            rabbit.is_buck = True
            rabbit.save()
        
         