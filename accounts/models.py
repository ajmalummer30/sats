
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.formfields import PhoneNumberField 
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    # Add extra fields
    age = models.PositiveIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    employee_id = models.CharField(max_length=20)
    station_name = models.ForeignKey('accounts.Station', on_delete=models.CASCADE,null=True)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,default=None,blank=True, related_name='managed_users')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
class Department(models.Model):
    Name = models.CharField(max_length=30)
    Dept_Head =models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.Name
class Station(models.Model):
    Name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
    

    
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()