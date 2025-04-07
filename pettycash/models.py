from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from accounts.models import CustomUser, Station
#from polls.models import Station





class Expense(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    claimant = models.CharField(max_length=100)
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE)
    Approved_status = models.BooleanField(default=False, null=True)
    upload_bill = models.FileField(upload_to='PettycashInvoices/',null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    approved_date = models.DateTimeField(default=None,null=True)
    # Add other expense details as needed

class ExpenseItem(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
class TravelClaim(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    days = models.DecimalField(max_digits=2,decimal_places=0)
    justification = models.CharField(max_length=255)
    accommodation = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    meals = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    transportation = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    miscellaneous = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    Total_Amount =models.DecimalField(max_digits=8, decimal_places=2)
    upload_bill = models.FileField(upload_to='travelclaimbills/',null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    status = models.BooleanField(default=False)
    approved_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    