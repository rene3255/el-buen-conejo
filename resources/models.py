from django.db import models

# Create your models here.
class State(models.Model):
    state = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = ('State')
        verbose_name_plural = ('States')
        ordering = ['state']
        
    def __str__(self):
        return self.state    

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_city')
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ('City')
        verbose_name_plural = ('Cities')
        ordering = ['city']
    
    def __str__(self):
        return self.city

class Breed(models.Model):
    breed = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)    
    
    class Meta:
        verbose_name = ('breed')
        verbose_name_plural = ('breeds')
        ordering = ['breed']
     
    def __str__(self):
        return self.breed    

class RabbitStatus(models.Model):
    status = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ('Rabbit status')
        verbose_name_plural = ('Rabbits Status')
        ordering = ['status']
    
    def __str__(self):
        return self.status