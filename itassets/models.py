
from django.utils import timezone
import datetime
from django.db import models
from accounts.models import CustomUser, Station
from simple_history.models import HistoricalRecords
from django.contrib.auth import get_user_model
from simple_history import register
from django.core.exceptions import ValidationError


# from polls.models import Station
from django.core.validators import FileExtensionValidator

# Create your models here.


class It_Brand(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand


class It_Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
    
class It_Model(models.Model):
    model_name = models.CharField(max_length=100)
    brand = models.ForeignKey(It_Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(It_Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='itassets/productimages', null=True, blank=True)

    def __str__(self):
        return f"{ self.model_name }"


class It_Device_Status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class Allocation_status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status
    
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100,null=True) # Vendor name
    vendor_contact = models.CharField(max_length=100, null=True, blank=True) # Vendor


    def __str__(self):
        return self.vendor_name


class It_Prodcuts(models.Model):

    brand = models.ForeignKey(It_Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(It_Category, on_delete=models.CASCADE)
    model = models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.CharField(max_length=100)
    Asset_tag = models.CharField(max_length=100, null=True, blank=True)
    supplier = models.CharField(max_length=100, null=True, blank=True)
    warranty_start_date = models.DateField(null=True, blank=True)
    warranty_end_date = models.DateField(null=True, blank=True)
    po_number = models.CharField(max_length=100, null=True, blank=True)
    processor = models.CharField(max_length=100, null=True, blank=True)
    ram = models.CharField(max_length=100, null=True, blank=True)
    harddisk = models.CharField(max_length=100, null=True, blank=True)
    operating_system = models.CharField(max_length=100, null=True, blank=True)
    status = models.ForeignKey(It_Device_Status, on_delete=models.CASCADE,blank=True)
    allocation_status = models.ForeignKey(Allocation_status, on_delete=models.CASCADE, max_length=20, default=1)
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now().date())
    file = models.FileField(upload_to='uploads/', null=True, blank=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    asset_remarks = models.TextField(blank=True, null=True)
    current_allocation = models.OneToOneField(
        'ItAssetAllocation',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='allocated_product'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    location = models.CharField(max_length=100,null=True, blank=True)
    device_model =models.ForeignKey(It_Model, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.serial_number


class ItAssetAllocation(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    serial_number = models.ForeignKey(It_Prodcuts, on_delete=models.CASCADE)
    allocation_date = models.DateTimeField()
    deallocation_date = models.DateTimeField(null=True, blank=True)


class CustomHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    model_name = models.CharField(max_length=255)
    instance_id = models.IntegerField()
    field_name = models.CharField(max_length=255)
    old_value = models.CharField(max_length=255)
    new_value = models.CharField(max_length=255)

class It_Mobile(models.Model):
    Itproduct = models.OneToOneField(It_Prodcuts, on_delete=models.CASCADE, related_name='mobile_phone')
    imei = models.CharField(max_length=15, unique=True,blank=True,null=True)

    def __str__(self):
        return self.Itproduct.serial_number
    
class CCTV(models.Model):
    it_product = models.OneToOneField(It_Prodcuts, on_delete=models.CASCADE, related_name='cctv')
    ip_address = models.GenericIPAddressField(blank=True,null=True)

    def __str__(self):
        return self.it_product.serial_number

def validate_file_size(value):
    filesize = value.size
    if filesize > 5 * 1024 * 1024:  # 5MB in bytes
        raise ValidationError("The maximum file size that can be uploaded is 5MB")

class MaintenanceRequest(models.Model):
    it_product = models.ForeignKey(It_Prodcuts, on_delete=models.CASCADE, related_name='maintenance_requests',null=True, blank=True)
    Created_By = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True)
    request_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor',null=True)
    status = models.CharField(max_length=20, choices=[('1', 'Pending'), ('2', 'Submitted to Vendor'), ('3', 'Completed')], default='1')
    Payment_Mode=models.CharField(max_length=20, choices=[('1', 'PO'), ('2', 'Cash'),('3', 'NA')], null=True,blank=True)
    po_number = models.CharField(max_length=50, null=True, blank=True) # Purchase Order number
    is_under_warranty = models.BooleanField(null=True) # Indicates if the asset is under warranty
    Warranty_type = models.CharField(max_length=20, choices=[('1', 'Full'), ('2', 'Partial')], null=True,blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    file = models.FileField(upload_to='itassets/maint_requests/', null=True, blank=True)
    is_Device_Repalced = models.BooleanField(null=True)
    Replaced_Device_Serial_Number = models.CharField(max_length=256,null=True,blank=True)
    Remarks =models.CharField(max_length=256,blank=True,null=True)

def __str__(self):
    return f"Maintenance for {self.it_product.serial_number} on {self.request_date}"

class Maint_Request_history(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    Request_number = models.ForeignKey(MaintenanceRequest, on_delete=models.CASCADE, related_name='Maint_Request_history',null=True, blank=True)
    status = models.CharField(max_length=256,null=True,blank=True)
    changes = models.TextField(null=True, blank=True)
