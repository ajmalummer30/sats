import datetime
from django.db import models
from django.dispatch import receiver
from accounts.models import CustomUser,Department
from django.utils import timezone
from import_export import resources
from accounts.models import Station
from django.core.validators import FileExtensionValidator
from django.core.validators import MinValueValidator, MaxValueValidator


class Fuel(models.Model):
    fueltype = models.CharField(max_length=100)
    
    def __str__(self):
        return self.fueltype

""" class Station(models.Model):
    stationname = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.stationname"""


""" class Subject(models.Model):
    name = models.CharField(max_length=100)
    Serial_Number =models.CharField(max_length=100,default=123)
    Capacity=models.CharField(max_length=100)
    Brand =models.CharField(max_length=100)
    Manufacture_Year =models.CharField(max_length=100,default=2016)
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE,null=True)
    fueltype = models.ForeignKey(Fuel, on_delete=models.CASCADE,null=True) """
    
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    Serial_Number =models.CharField(max_length=100,default=123)
    Capacity=models.CharField(max_length=100)
    Brand =models.CharField(max_length=100)
    Manufacture_Year =models.CharField(max_length=100,default=2016)
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE,null=True)
    fueltype = models.ForeignKey(Fuel, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name
    
    

class GeneralQuestion(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

""" class SubjectSpecificQuestion(models.Model):
    subject = models.ForeignKey(Equipment, on_delete=models.CASCADE,null=True)
    fueltype = models.ForeignKey(Fuel, on_delete=models.CASCADE,null=True)
    text = models.TextField(verbose_name='Enter New question')

    def __str__(self):
        return self.text """
    
class EquipmentSpecificQuestion(models.Model):
    subject = models.ForeignKey(Equipment, on_delete=models.CASCADE,null=True)
    fueltype = models.ForeignKey(Fuel, on_delete=models.CASCADE,null=True)
    text = models.TextField(verbose_name='Enter New question')

    def __str__(self):
        return self.text
    
class ChecklistDetails(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=timezone.localtime(timezone.now()).strftime('%H:%M:%S'))
    
    def __str__(self):
        return f"{self.equipment} - {self.date} - {self.user}- {self.time}"
    

class GenQuestionResponse(models.Model):
    question = models.ForeignKey(GeneralQuestion, on_delete=models.CASCADE,null=True)
    response = models.CharField(max_length=100)
    checklistid = models.ForeignKey(ChecklistDetails, on_delete=models.CASCADE,null=True)

class SubQuestionResponse(models.Model):
    question = models.ForeignKey(EquipmentSpecificQuestion, on_delete=models.CASCADE,null=True)
    response = models.CharField(max_length=100)
    checklistid = models.ForeignKey(ChecklistDetails, on_delete=models.CASCADE,null=True)


class Contractor(models.Model):
    Company_Name = models.CharField(max_length=100)
    CR_Number = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.Company_Name

class Workers(models.Model):
    Employee_name = models.CharField(max_length=100)
    Iqama_Number = models.CharField(max_length=10)
    Phone_number = models.CharField(max_length=10)
    upload_Iqama = models.FileField(upload_to='WorkPermit_iqama/',null=True,blank=True)

    def __str__(self):
        return f"{self.Employee_name} {self.Iqama_Number}"
    

class Fa_Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class Fa_SubCategory(models.Model):
    category = models.ForeignKey(Fa_Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"
    
class Fa_Contract(models.Model):
    FREQUENCY_CHOICES = [
        (1, '30 days'),
        (2, '90 days'),
        (3, '60 days'),
        (4, '120 days'),
        (5, '15 days'),
    ]
    
    STATUS_CHOICES = [
        (1, 'Active'),
        (2, 'Inactive'),
    ]

    contract_reference_number = models.CharField(max_length=100, unique=True)
    Department=models.ForeignKey(Department, related_name='Fa_Department', on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Fa_Category, related_name='Fa_category', on_delete=models.CASCADE,null=True)
    subcategory = models.ManyToManyField(Fa_SubCategory,null=True)
    contractor = models.ForeignKey(Contractor, related_name='contracts', on_delete=models.CASCADE,null=True)
    Account_Manager = models.CharField(max_length=256,null=True,)
    Contact_Details = models.CharField(max_length=256,null=True,)
    Email_ID = models.EmailField(null=True,)
    start_date = models.DateField(null=True,)
    end_date = models.DateField(null=True,)
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    no_of_pm_visits = models.IntegerField(null=True)
    frequency = models.IntegerField( choices=FREQUENCY_CHOICES,null=True)
    Created_By = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    request_date = models.DateTimeField(auto_now_add=True)
    PO_Number = models.CharField(max_length=256,null=True)
    PO_copy = models.FileField(upload_to='contracts/po/', null=True, blank=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    contract_copy = models.FileField(upload_to='contracts/contractscopy/', null=True, blank=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    Remarks = models.TextField(blank=True,null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return self.contract_reference_number
    
class Fa_ContractFile(models.Model):
    contract = models.ForeignKey(Fa_Contract, related_name='Fa_ContractFile', on_delete=models.CASCADE)
    file = models.FileField(upload_to='contracts/common/', null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    filename = models.CharField(max_length=255,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Created_By = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True)

class Workorder(models.Model):
    TYPE_CHOICES = [
        (1, 'PM'),
        (2, 'CM'),
        (3, 'OTHER'),
    ]
    Type_of_work = models.IntegerField(choices=TYPE_CHOICES)
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE,null=True)
    Created_By = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #PM_order = models.ForeignKey('PreventiveMaintenance', null=True, blank=True, on_delete=models.SET_NULL, related_name='workorders_pm')
    #CM_order = models.ForeignKey('CorrectiveMaintenance', null=True, blank=True, on_delete=models.SET_NULL, related_name='workorders_cm')

    def __str__(self):
        return str(self.id)

class PreventiveMaintenance(models.Model):
    work_order = models.OneToOneField(Workorder, on_delete=models.CASCADE,null=True ,related_name='preventivemaintenance')
    contract = models.ForeignKey(Fa_Contract, on_delete=models.CASCADE)
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE,null=True)
    Created_By = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True)
    uploaded_at = models.DateField(default=timezone.now)
    pm_datetime = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=256)
    next_pm_date = models.DateField(null=True, blank=True)
    email_sent = models.BooleanField(default=False)
    #Created_By = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True)
    def __str__(self):
        return str(self.contract)


class Fa_PM_ContractFile(models.Model):
    pm = models.ForeignKey(PreventiveMaintenance, related_name='Fa_PM_ContractFile', on_delete=models.CASCADE)
    file = models.FileField(upload_to='contracts/pmattachment', null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    filename = models.CharField(max_length=255,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Created_By = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True)
    
class PM_Comment(models.Model):
    pm_record = models.ForeignKey(PreventiveMaintenance, related_name='PM_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Comment by {self.user} on {self.pm_record}'

class CorrectiveMaintenance(models.Model):
    work_order = models.OneToOneField(Workorder, on_delete=models.CASCADE,null=True,related_name='correctivemaintenance')
    Scope_of_Work = models.CharField(max_length=256,null=True)
    contract = models.ForeignKey(Fa_Contract, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, related_name='Fa_CM_contractor', on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Fa_Category, related_name='Fa_CM_category', on_delete=models.CASCADE,null=True)
    subcategory = models.ManyToManyField(Fa_SubCategory,null=True)
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE,null=True)
    purchase_order = models.CharField(max_length=100,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    uploaded_at = models.DateField(default=timezone.now)
    cm_datetime = models.DateTimeField(auto_now_add=True)
    Created_By = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True)
    def __str__(self):
        return str(self.id)
    
class CM_Comment(models.Model):
    cm_record = models.ForeignKey(CorrectiveMaintenance, related_name='CM_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Comment by {self.user} on {self.cm_record}'


class Fa_CM_ContractFile(models.Model):
    cm = models.ForeignKey(CorrectiveMaintenance, related_name='Fa_CM_ContractFile', on_delete=models.CASCADE)
    file = models.FileField(upload_to='contracts/cmattachment', null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    filename = models.CharField(max_length=255,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Created_By = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True)
    

    
class Workpermit(models.Model):
    work_order = models.ForeignKey(Workorder, related_name='workpermits', on_delete=models.CASCADE,null=True)
    start_date =models.DateField()
    end_date =models.DateField()
    created_date = models.DateField(default=datetime.date.today)
    Created_time = models.TimeField(default=timezone.localtime())
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE,null=True)
    Contractor_Name = models.CharField(max_length=100,blank=True,null=True)
    Contracting_Company_Name =models.ForeignKey(Contractor, on_delete=models.CASCADE)
    workers = models.ManyToManyField(Workers)
    Staff_in_charge = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=10)
    Iqama_number = models.CharField(max_length=10,blank=True,null=True)
    Employee_Count = models.IntegerField()
    Description = models.TextField()
    Additional_notes = models.TextField()
    Tools = models.TextField()
    upload_Iqama = models.FileField(upload_to='WorkPermit_iqama/',null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel") 
     
     
class NatureOfInjury(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Incident(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    nature_of_injury = models.ManyToManyField(NatureOfInjury)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Incident {self.pk}"
    
def get_current_time():
    return timezone.localtime().time()



class GatePassModel(models.Model):

    ISSUE_CHOICES = (
        (0, 'Entry'),
        (1, 'Exit'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Issue_Date =models.DateField(default=datetime.date.today)
    Created_time = models.TimeField(default=get_current_time)
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE,null=True)
    Mode = models.IntegerField(choices=ISSUE_CHOICES, default=1) 
    Return_status = models.CharField(max_length=5)
    Return_date = models.DateField(null=True)
    Company_Name = models.CharField(max_length=100)
    Driver_name = models.CharField(max_length=100)
    Iqama_Number = models.CharField(max_length=10)
    Contact_Details = models.CharField(max_length=10)
    Vehicle_Plate_Number = models.CharField(max_length=8)
    Item_Description=models.TextField(null=True)
    Reason = models.TextField(null=True)
    image1 = models.ImageField(upload_to='gatepass/', null=True, blank=True)



class Gatepass_Items_Model(models.Model):
    GatePass = models.ForeignKey(GatePassModel, on_delete=models.CASCADE)
    Description =models.CharField(max_length=256)
    qty = models.IntegerField()
    Remarks = models.TextField()

        

class NewMaintanence(models.Model):
    # Linking to a work order with a one-to-one relationship
    work_order = models.OneToOneField(Workorder, on_delete=models.CASCADE, null=True, related_name='newmaintenance')

    # Basic fields
    scope_of_work = models.CharField(max_length=256, null=True)
    contract = models.ForeignKey(Fa_Contract, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, related_name='Fa_New_contractor', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Fa_Category, related_name='Fa_New_category', on_delete=models.CASCADE, null=True)

    # Many-to-Many relation (remove null=True, since ManyToManyField does not support it)
    subcategory = models.ManyToManyField(Fa_SubCategory, blank=True)

    # Station and purchase order fields
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE, null=True)
    purchase_order = models.CharField(max_length=100, null=True)

    # Financial information
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    # Date and Time fields
    uploaded_at = models.DateField(default=timezone.now)
    cm_datetime = models.DateTimeField(auto_now_add=True)

    # Reference to the user who created the entry
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    # String representation of the model
    def __str__(self):
        return f"Corrective Maintenance for Work Order {self.work_order}"
    
    
    
class Fa_New_ContractFile(models.Model):
    New = models.ForeignKey(NewMaintanence, related_name='Fa_New_ContractFile', on_delete=models.CASCADE)
    file = models.FileField(upload_to='contracts/Newattachment', null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    filename = models.CharField(max_length=255,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Created_By = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True)
    
    
class New_Comment(models.Model):
    New_record = models.ForeignKey(NewMaintanence, related_name='New_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Comment by {self.user} on {self.New_record}'
