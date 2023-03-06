from django.db import models

# Create your models here.

class Doe(models.Model):
    doe_name = models.CharField(max_length=30)
    selection_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.doe_name