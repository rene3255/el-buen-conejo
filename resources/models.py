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
    state_id = models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_city')
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ('City')
        verbose_name_plural = ('Cities')
        ordering = ['city']
    
    def __str__(self):
        return self.city
  