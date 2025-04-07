from django.db.models.signals import post_save,post_delete,pre_save
from .views import my_signal
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import CustomHistory, It_Prodcuts, Maint_Request_history, MaintenanceRequest
from itassets.models import It_Prodcuts, ItAssetAllocation







@receiver(post_save, sender=ItAssetAllocation)
def post_save_product(sender, instance, created, **kwargs):
    if created:
        try:
            print('instance.id')
            status_instance = instance.id
            asset_details = It_Prodcuts.objects.get(id=instance.serial_number)
            print(asset_details)
        except It_Prodcuts.DoesNotExist:
            # Handle the case where a matching Status instance is not found
            pass


    
""" @receiver([post_save, post_delete], sender=It_Prodcuts)
def my_signal_handler(sender, instance, **kwargs):
    arg1 = kwargs.get('arg1')
    print(arg1) """
    
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    user = kwargs.get('arg1')
    instance = kwargs.get('instance')
    model_name = sender.__name__
   
 
    

@receiver(pre_save, sender=MaintenanceRequest)
def track_status_change(sender, instance, **kwargs):
    if instance.pk:
        old_instance = MaintenanceRequest.objects.get(pk=instance.pk)
        changes = {}
        for field in instance._meta.fields:
            if getattr(old_instance, field.name) != getattr(instance, field.name):
                changes[field.name] = {
                    'old_value': getattr(old_instance, field.name),
                    'new_value': getattr(instance, field.name)
                }
        if changes:
            user = instance.Created_By
            history_entry = Maint_Request_history.objects.create(
                user=user,
                timestamp=instance.request_date,
                Request_number=instance,
                status=instance.status,
                changes=changes
            )
        """ if old_instance.status != instance.status:
            user=instance.Created_By
            Maint_Request_history.objects.create(
                user=instance.Created_By,
                timestamp=instance.request_date,
                Request_number=instance,  # Assign the MaintenanceRequest instance
                status=instance.status
            ) """

   
    
   
    
