from operator import mod
from turtle import heading
from django.db import models

# Create your models here.

class mindset(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    date=models.DateField(auto_created=True)
    brother=models.CharField(max_length=100,blank=True,null=True)
    father=models.CharField(max_length=100,blank=True,null=True)
    mother=models.CharField(max_length=100,blank=True,null=True)
    heading=models.CharField(max_length=100,blank=True,null=True)
    heading=models.CharField(max_length=100,blank=True,null=True)
    heading=models.CharField(max_length=100,blank=True,null=True)
    heading=models.CharField(max_length=100,blank=True,null=True)
    heading=models.CharField(max_length=100,blank=True,null=True)
    veera=models.CharField(max_length=200,blank=True,null=True)
    sheera=models.CharField(max_length=100,null=True,blank=True)
    sheera1=models.CharField(max_length=100,null=True,blank=True)
    
    description1=models.CharField(max_length=100,blank=True,null=True)
    description2=models.CharField(max_length=100,blank=True,null=True)
    description3=models.CharField(max_length=100,blank=True,null=True)
    description4=models.CharField(max_length=100,blank=True,null=True)
    description5=models.CharField(max_length=100,blank=True,null=True)

    
