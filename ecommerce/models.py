from turtle import heading
from django.db import models

# Create your models here.

class mindset(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    date=models.DateField(auto_created=True)
    heading=models.CharField(max_length=100,blank=True,null=True)