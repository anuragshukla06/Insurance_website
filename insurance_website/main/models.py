from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip = models.IntegerField()
    profilePic = models.ImageField(null=True)

class Insurance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Animal = models.CharField(max_length=200, default="None")
    Request = models.BooleanField(default=True)
    Active = models.BooleanField(default=False)
    Plan = models.IntegerField()
    StartDate = models.DateTimeField(default=datetime.datetime.now())
    EndDate = models.DateTimeField(default=datetime.datetime.now())
    Claimed = models.BooleanField(default=False)



class Claims(models.Model):
    Insurance_claimed = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    Claimed_date = models.DateTimeField(default=datetime.datetime.now())
    Handled = models.BooleanField(default=False)