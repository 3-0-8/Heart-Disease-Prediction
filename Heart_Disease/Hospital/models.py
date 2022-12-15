from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Queries(models.Model):
    user=models.CharField(max_length=200,blank=True,null=True)
    date=models.CharField(max_length=200,blank=True,null=True)
    time=models.CharField(max_length=200,blank=True,null=True)
    result=models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.user
