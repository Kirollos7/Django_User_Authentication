from django.db import models
# one to one field 
from django.contrib.auth.models import UserManager,User 
# Create your models here.
# Overload on Django User Model 
# 4 Types in Extend 
    # - Proxy Model
    # - One-To-One Field
    # - Extend Abstract Base User
    # - Extend Abstract USer
''' username , password , first name , last name , email   '''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    # image
    # job
    def __str__(self):
        return str(self.user)
         