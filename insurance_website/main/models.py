from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip = models.IntegerField()