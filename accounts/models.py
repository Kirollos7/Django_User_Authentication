from django.db import models
# one to one field 
from django.contrib.auth.models import UserManager,User 
from django.db.models.signals import Signal , post_save
from django.dispatch import receiver
# Create your models here.
# Overload on Django User Model 
# 4 Types in Extend 
    # - Proxy Model
    # - One-To-One Field
    # - Extend Abstract Base User
    # - Extend Abstract USer
    # signal  2 event happend one dependand to anther
''' username , password , first name , last name , email   '''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    # image
    # job
    def __str__(self):
        return str(self.user)
         
@receiver(post_save, sender = User)
def create_user_profile(sender , instance , created , **kwargs):
    if  created:
        Profile.objects.create(
            user = instance
        )
    
    
    
    
    
    
    
    