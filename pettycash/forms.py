from django import forms
from django.forms import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.core.exceptions import ValidationError
#from polls.models import Station
from accounts.models import Station
from .models import Expense, ExpenseItem, TravelClaim
from django.contrib.admin.widgets import AdminDateWidget

class ExpenseForm(forms.ModelForm):
    
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type': 'text'}),label='Note' )
    claimant = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type': 'text', 'readonly': 'readonly'}),label='Claimant Name' )
    Manager_Email =forms.EmailField(label='Manager Email',widget=forms.EmailInput(attrs={'class': 'form-control','type': 'email','readonly': 'readonly'})) 
    class Meta:
        model = Expense
        fields = ['claimant','description','upload_bill']
        labels = {
                     'upload_bill': 'Upload Bill'
                }
        widgets= {
            'upload_bill': forms.FileInput(attrs={'class': 'form-control'}),
        }
    

class ExpenseItemForm(forms.ModelForm):
    class Meta:
        model = ExpenseItem
        fields = ['item_name', 'quantity', 'unit_price','amount']
    def __init__(self, *args, **kwargs):
        super(ExpenseItemForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs['disabled'] = True
        self.fields['amount'].required = False 
        

ExpenseItemFormSet = inlineformset_factory(Expense, ExpenseItem, form=ExpenseItemForm, extra=1,can_delete=True, can_delete_extra=True)


class Travelclaims(forms.Form):
    
    station_name =forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),label='STATION NAME',queryset=Station.objects.all(), empty_label="Select Station",) 
    
class TravelclaimForm(forms.ModelForm):
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
            
        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError('End date should be after start date.')
            
        return cleaned_data
        
    
    class Meta:
        model = TravelClaim
        fields = '__all__'
        exclude= ['user','Total_Amount','status','approved_date','created_date']
        
        labels = {

            'station': 'station',
            'start_date': 'start date',
            'end_date': 'End date',
            'days': 'No of Days',
            'justification': 'justification',
            'accommodation': 'accommodation (SAR)',
            'transportation': 'transportation (SAR)',
            'meals': 'meals(SAR)',
            'miscellaneous': 'miscellaneous (SAR)',
            'upload_bill' : 'upload the combined bills as PDF format'
            
           
        }
        widgets = {
           
            'start_date': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'days': forms.NumberInput(attrs={'type': 'number','class': 'form-control'}),
            'justification': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'accommodation': forms.NumberInput(attrs={'class': 'form-control'}),
            'transportation': forms.NumberInput(attrs={'class': 'form-control'}),
            'meals': forms.NumberInput(attrs={'class': 'form-control'}),
            'miscellaneous': forms.NumberInput(attrs={'class': 'form-control'}),
            'upload_bill': forms.FileInput(attrs={'class': 'form-control'}),
            
            
        }
        error_messages = {
             'start_date': {
                'required': 'Start date is required.'
            },
            'end_date': {
                'required': 'End date is required.'
            },
            'justification': {
                'required': 'Justification is required.'
            }
        }
    
        
    
        
class travelclaiminfo(forms.Form):
    Employee_Name= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control col-md-4'}))
    Employee_Email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control col-md-4'}))
    Station = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control col-md-4'}))
    Manager_Email = forms.EmailField(label='Manager Email',widget=forms.EmailInput(attrs={'readonly': 'readonly','class': 'form-control col-md-4'}))     
    def __init__(self,user, *args, **kwargs):
        super(travelclaiminfo, self).__init__(*args, **kwargs)
        self.fields['Employee_Name'].initial = f"{user.first_name} {user.last_name}"
        self.fields['Employee_Email'].initial = user.email
        self.fields['Station'].initial = user.station_name
        self.fields['Manager_Email'].initial = user.manager.email
        
        
        

 
class ExpenseFilterForm(forms.ModelForm):
    
    class Meta:
        model = Expense
        fields = '__all__'
        widgets={
        'station_name': forms.Select(attrs={'class':'form-select'}),
        'employee': forms.Select(attrs={'class':'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['station_name'].required = False
        self.fields['employee'].required = False

    