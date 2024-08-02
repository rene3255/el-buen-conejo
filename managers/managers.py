from django.db import models
class RecordManager(models.Manager):
    def register_active(self):
        return self.filter(is_active=True)
      