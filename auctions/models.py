from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.utils import timezone


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=30, unique=True)

    def __str__ (self):
        return f"{self.category}"

class Listing(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    initialBid = models.FloatField()
    currentBid =models.FloatField(null=True, blank=True)
    image = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True, related_name="category_list")
    date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="creator_listings", null=True)
    
    def __str__(self):
        return {
            'id': self.id   } 

class Bid(models.Model):
    bid_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="userbid")
    bid_listing = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True, related_name="listingBid")
    date = models.DateTimeField(auto_now=True)
    offer = models.FloatField()

    def __str__(self):
        return f"{self.bid_listing} {self.offer}"