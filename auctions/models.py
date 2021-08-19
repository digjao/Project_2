from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    initialBid = models.FloatField()
    image = models.URLField(blank=True)
    category = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return f"item {self.id} : {self.title}"