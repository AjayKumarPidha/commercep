import re
from urllib import request
from django.shortcuts import render
from django import views

# Create your views here.
class com(views):
     def get(self,request):
        return render("hello")
