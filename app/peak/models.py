from django.db import models
from django.conf import settings
from django.utils import timezone

class Peak(models.Model):
    """Tag to be used for a recipe"""

    lat = models.FloatField()
    lon = models.FloatField()
    altitude = models.FloatField()

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
