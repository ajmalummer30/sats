
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form
from phonenumber_field.formfields import PhoneNumberField

from accounts.models import CustomUser,Profile
from polls.models import Station
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
  
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }),label='First Name')
    last_name = forms.CharField(label='last Name')
    employee_id = forms.CharField(label='Employee Id')  
    phone_number = PhoneNumberField(label='Mobile Number',region='SA')
    username = forms.CharField(label='Username', min_length=5, max_length=150,) 
    station_name = forms.ModelChoiceField(label='STATION NAME',queryset=Station.objects.all(), empty_label="Select a model",) 
    email = forms.EmailField(label='Email')  
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
  
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if CustomUser.objects.filter(username=username).count():
            raise ValidationError("User Already Exists")
        return username

    def clean_employee_id(self):
        employee_id = self.cleaned_data['employee_id'].lower()
        if CustomUser.objects.filter(employee_id=employee_id).count():
            raise ValidationError("Employee ID Already Exists")
        return employee_id
  
    
     
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        # Perform custom validation for the phone number if needed
        # For example, you can check the length or format
        if len(str(phone_number)) < 10:
            raise forms.ValidationError("Phone number is too short.")
        return phone_number
  
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if CustomUser.objects.filter(email=email).exists():
                raise forms.ValidationError('This email address is already associated with an account. Please use a different ones.')
        else:
            return email
    
    
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    """ def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1'] ,
            
              
        )  
        return user   """
    class Meta:
        model=CustomUser
        #this is only required to rearrange the order of fields defined at top.
        # otherwise explicity mentioned fields are enough and no need to mention meta
        fields = ['first_name','last_name','employee_id','username','email','password1','password2','phone_number','station_name','manager'] 
        
    
        
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( 'location', 'birth_date')
        
class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check if the provided email exists in your system or any other custom validations
        if not CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email address is not registered.")
        return email

