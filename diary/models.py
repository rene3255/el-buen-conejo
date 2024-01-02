from django.db import models
from farms.models import ProducerProfile
from managers.managers import RecordManager


# Create your models here.
class Diary(models.Model):
    activity_date = models.DateField()
    activity = models.TextField(max_length=255)
    costs = models.DecimalField(
        max_digits=10, decimal_places=2, default="0.00", null=True, blank=True
    )
    farm = models.ForeignKey(ProducerProfile, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "activity"
        verbose_name_plural = "activities"
        ordering = ("-activity_date",)

    def __str__(self):
        return self.activity

    objects = RecordManager()
