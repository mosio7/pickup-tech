from time import timezone
from django.db import models
from django.utils import timezone

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=50)
    weight = models.CharField(max_length=20)
    description = models.TextField()
    amount= models.IntegerField()

class user(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    ID = models.IntegerField()
    description = models.TextField()
    address = models.TextField()
    Email = models.EmailField()
    phhone = models.IntegerField()
    birthday = models.DateField()
    publish = models.DateField(default= timezone)


class address(models.Model):
    address = models.TextField()
    description = models.TextField()
    phone = models.IntegerField()
    postal_code = models.IntegerField()


