from django.db import models
from django.utils import timezone

class Post(models.Model):
    K_time = models.CharField(max_length=200)
    K_location = models.CharField(max_length=200)
    K_death = models.CharField(max_length=200)
    K_injure = models.CharField(max_length=200)
#    class Meta:
#        ordering = ('-pub_date',)

    def __str__(self):
        return str(self.id)

