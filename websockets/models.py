
from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser
from myproject import settings
from django.db.models.signals import post_save
from django.dispatch import receiver





class Counter(models.Model):
    name = models.CharField(max_length=100)
    # other fields as necessary

    def __str__(self):
        return self.name

class Web_User_Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='Web_profile')
    counter = models.OneToOneField('Counter', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.user) 
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Web_User_Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'Web_profile'):
        instance.Web_profile.save()

class Ticket(models.Model):
    ticket_number = models.IntegerField()
    issued_at = models.DateTimeField(auto_now_add=True)
    counter_number = models.PositiveIntegerField(blank=True,null=True)
    called = models.BooleanField(default=False)
    mobile_number=models.IntegerField(null=True)
    # Add other fields if necessary (e.g., counter, status, etc.)

    def __str__(self):
         return f"Ticket {self.ticket_number} for Counter {self.counter_number}"