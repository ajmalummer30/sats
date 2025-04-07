
from unittest.util import _MAX_LENGTH
from django.db import models
from traitlets import default


from accounts.models import Station

# Create your models here.

class In_IncidentType(models.Model):   
    text = models.CharField(max_length=20)
    
    def __str__(self):
        return self.text
    
class WhetherCondition(models.Model):   
    text = models.CharField(max_length=20)
    
    def __str__(self):
        return self.text
class In_Category(models.Model):   
    text = models.CharField(max_length=20)
    
    def __str__(self):
        return self.text
    
class In_Visibility(models.Model):   
    text = models.CharField(max_length=20)
    
    def __str__(self):
        return self.text
    
class In_SurfaceCondition(models.Model):   
    text = models.CharField(max_length=20)
    
    def __str__(self):
        return self.text


    def __str__(self):
        return self.text
    
class In_NatureOfInjury(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
    
class In_BodyParts(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
    
class DriverInvolved(models.Model):
    name = models.CharField(max_length=100)
    iqama_id =models.DecimalField(max_digits=10,decimal_places=0,null=True)
    
    def __str__(self):
            return self.name

class Country(models.Model):
    text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.text
    
class States(models.Model):
    State = models.CharField(max_length=100)
    country =models.ForeignKey(Country, on_delete=models.CASCADE)


    def __str__(self):
        return self.State
        
    
class Employeesinvolved(models.Model):
        name = models.CharField(max_length=100,null=True)
        iqama_id =models.DecimalField(max_digits=10,decimal_places=0,default=2425924541)
        department = models.CharField(max_length=100,null=True,blank=True)
        designation = models.CharField(max_length=100,null=True,blank=True)
        gaca_id =models.DecimalField(max_digits=10,null=True,blank=True,decimal_places=0)
        image = models.ImageField(upload_to='safety_images/', null=True, blank=True)
        upload_Iqama = models.FileField(upload_to='safety_images/',null=True,blank=True)
        driver_name = models.ManyToManyField(DriverInvolved, related_name='incidents_driver',null=True,blank=True)
        country =models.ForeignKey(Country, on_delete=models.CASCADE,null=True,blank=True)
        states =models.ForeignKey(States, on_delete=models.CASCADE,null=True,blank=True)
        
        
        # Add any other relevant fields for the Employee model

        def __str__(self):
            return self.name
        

class In_Incidents(models.Model):
    type = models.ForeignKey(In_IncidentType,on_delete=models.CASCADE )
    Location =models.CharField(max_length=100)
    whether_condition =models.ForeignKey(WhetherCondition, on_delete=models.CASCADE)
    category =models.ForeignKey(In_Category, on_delete=models.CASCADE)
    station =models.ForeignKey(Station, on_delete=models.CASCADE)
    visibility =models.ForeignKey(In_Visibility, on_delete=models.CASCADE)
    date_of_occurance = models.DateField()
    time_of_occurance=models.TimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    surface_condition =models.ForeignKey(In_SurfaceCondition, on_delete=models.CASCADE)
    employees_name = models.ManyToManyField(Employeesinvolved, related_name='incidents')
    driver_name = models.ManyToManyField(DriverInvolved, related_name='incidents')
    nature_of_injury = models.ManyToManyField(In_NatureOfInjury)
    bodyparts_affected = models.ManyToManyField(In_BodyParts)
    Summary =models.CharField(max_length=256)
    contributory_factors =models.CharField(max_length=256,)
    corrective_measurments =models.CharField(max_length=256,)
    preventive_measures = models.CharField(max_length=256,)
    image1 = models.ImageField(upload_to='safety_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='safety_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='safety_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='safety_images/', null=True, blank=True)
    
    
    
    def __str__(self):
        return str(self.id)
    
    



