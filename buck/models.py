from django.db import models

# Create your models here.
class Buck(models.Model):
    buck_name = models.CharField(max_length=30)
    selection_date = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.buck_name