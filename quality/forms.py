from cProfile import label
from django import forms
from .models import DriverInvolved, In_Incidents

class IncidentReportingForm(forms.ModelForm):
    class Meta:
        model = In_Incidents
        fields = '__all__'
        exclude =['created_date']
        widgets = {
            'type': forms.Select(attrs={'class':'form-select'}),
            'Location' : forms.TextInput(attrs={'class':'form-control'}),
            'whether_condition': forms.Select(attrs={'class':'form-select'}),
            'category': forms.Select(attrs={'class':'form-select'}),
            'station': forms.Select(attrs={'class':'form-select'}),
            'visibility': forms.Select(attrs={'class':'form-select'}),
            'date_of_occurance': forms.DateInput(attrs={'type': 'date','class':'form-select'}),
            'time_of_occurance': forms.TimeInput(attrs={'type': 'time','class':'form-select'}),
            'surface_condition': forms.Select(attrs={'class':'form-select'}),
            'nature_of_injury': forms.CheckboxSelectMultiple(),
            #'bodyparts_affected': forms.SelectMultiple(attrs={'id':'body_parts','class':'form-control'}),
            'bodyparts_affected': forms.CheckboxSelectMultiple(),
            'driver_name': forms.SelectMultiple(attrs={'id':'driver_name','class':'form-control'}),
            'employees_name': forms.SelectMultiple(attrs={'id':'employee_name','class':'form-control'}),
            'Summary' : forms.Textarea(attrs={'class':'form-control','rows':'2'}),
            'contributory_factors' : forms.Textarea(attrs={'class':'form-control','rows':'2'}),
            'corrective_measurments' : forms.Textarea(attrs={'class':'form-control','rows':'2'}),
            'preventive_measures' : forms.Textarea(attrs={'class':'form-control','rows':'2'}),
            'image1': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'image2': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'image3': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'image4': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            
        }
        labels={
            
            'type': 'Type' ,
            'Location' : 'Location' ,
            'whether_condition' :'whether Condition',
            'category':'Category',
            'station':'Station' ,
            'visibility' :'Visibility',
            'date_of_occurance' : 'Date of Occurance' ,
            'time_of_occurance' : 'Time of Occurance',
            'surface_condition' : 'Surface Condition',
            'employees_name' : 'Employee Name',
            'driver_name' :'Driver Name',
            'nature_of_injury' : 'Nature Of Injury',
            'bodyparts_affected' : 'Body Parts Affected',
            'Summary' : 'Summary',
            'contributory_factors' : 'contributory factors',
            'corrective_measurments':'corrective measurments',
            'preventive_measures':'preventive measures'
            
        }

    """ def __init__(self, *args, **kwargs):
        super(IncidentReportingForm, self).__init__(*args, **kwargs) """

class DriverForm(forms.ModelForm):
    
    class Meta:
        model = DriverInvolved
        fields = '__all__'
        
    def clean_iqama_id(self):
        iqama_id = self.cleaned_data['iqama_id']
        if DriverInvolved.objects.filter(iqama_id=iqama_id).exists():
            raise forms.ValidationError('IQAMA ID exists.')
        return iqama_id
    
    
      