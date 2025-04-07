

from django import forms

from polls.models import CM_Comment, Contractor, CorrectiveMaintenance, Equipment, EquipmentSpecificQuestion, Fa_CM_ContractFile, Fa_Category, Fa_Contract, Fa_ContractFile, Fa_New_ContractFile, Fa_PM_ContractFile, Fa_SubCategory, GatePassModel, Gatepass_Items_Model, Incident, New_Comment, NewMaintanence, PM_Comment, PreventiveMaintenance, Workers, Workpermit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.db.models import Value
from django.db.models.functions import Concat
from django import forms
from django.utils.timezone import localtime
from django.utils import timezone




class SubjectDropdownForm(forms.Form):
    
      
    #subject = forms.ModelChoiceField(queryset=Subject.objects.all(), empty_label="Select a model",widget=forms.Select(attrs={'id':'subject-dropdown'}))
  
    def __init__(self, user, *args, **kwargs):
        super(SubjectDropdownForm, self).__init__(*args, **kwargs)
        # Get the station code for the logged-in user
        station_code = user.station_name
        # Filter equipment based on the station code
        equipment_list = Equipment.objects.filter(station_name=station_code)
        # Create choices for the dropdown
        choices = [(None, 'Select a model')]
        choices +=  [(equip.id, equip.name) for equip in equipment_list]
        # Create the dropdown field
        self.fields['subject'] = forms.ChoiceField(choices=choices)
        self.fields['subject'].label = "Select Equipment"
        self.fields['subject'].widget.attrs.update({'id': 'subject-dropdown'})



class GenQuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(GenQuestionForm, self).__init__(*args, **kwargs)
        for question in questions:
            self.fields[f'answer1_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=[('1', 'Yes'), ('2', 'No')],
                widget=forms.RadioSelect(),
                required=True
            )
            
class SubQuestionForm(forms.Form):
    def __init__(self,subject, *args, **kwargs):
        super(SubQuestionForm, self).__init__(*args, **kwargs)
        #questions = kwargs.pop('questions')
        fueltype_value = subject.fueltype
        Subjquestions = EquipmentSpecificQuestion.objects.filter(fueltype=fueltype_value)
        for question in Subjquestions:
                field_id = f'answer2_{question.id}'
                self.fields[field_id] = forms.ChoiceField(
                    label=question.text,
                    choices=[('1', 'Yes'), ('2', 'No')],
                    widget=forms.RadioSelect(),
                    
                    )
    
class SubjectQuestionFrom(forms.ModelForm):
    
      class Meta:
        model = EquipmentSpecificQuestion
        fields = ['text']
        #exclude=['work_order']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Enter New question'}),
            # Define other widgets for other fields if needed


        }
class WorkPermitForm(forms.ModelForm):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['workers'].queryset = Workers.objects.all().annotate(Employee_nam=Concat('Employee_name', Value(' '), 'Iqama_Number'))
 

        

    def clean_upload_Iqama(self):
        upload_Iqama = self.cleaned_data.get('upload_Iqama')
        if upload_Iqama:
            if not upload_Iqama.name.endswith('.pdf'):
                raise forms.ValidationError("Please upload only PDF files.")
        return upload_Iqama
    
   
    
    class Meta:
        model = Workpermit
        fields = '__all__'
        exclude = ['Created_time','Contractor_Name','upload_Iqama','work_order']
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control','type': 'date',}),
            'end_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'created_date': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'Phone_number': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '1'}),
            'Iqama_number': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '1'}),
            'Description': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'cols': 40}),
            'Additional_notes': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'cols': 40}),
            'Tools': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'cols': 40}),
            'upload_Iqama': forms.FileInput(attrs={'class': 'form-control'}),
            'workers': forms.SelectMultiple(attrs={'class': 'form-control','id':'id_workers'}),
            'Contracting_Company_Name': forms.Select(attrs={'class': 'form-control'}),
            'station_name': forms.Select(attrs={'class':'form-select'}),
            'Staff_in_charge': forms.TextInput(attrs={'class': 'form-control'}),
            'Employee_Count': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '1'}),

            
            
            # Replace 'your_date_field_name' with the actual name of your date field in the model
            # 'attrs': {'type': 'date'} specifies the use of a date picker in HTML5
        }
        labels = {
            'Description': 'Scope of Work',
            'Contractor_Name': 'Company Name',
            'Staff_in_charge': 'Staff In Charge',
            'Contractor_Name' : 'Vendor Company Name',
            'Staff_in_charge' : 'Vendor Staff In charge',
            'upload_Iqama' : 'Upload Iqama Copy'
    
        }
        validators = {
            'upload_Iqama': [FileExtensionValidator(allowed_extensions=['pdf'], message='Please upload only PDF files.')]
        }
        
        
class WorkPermitFilterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['station_name'].required = False
        self.fields['Contracting_Company_Name'].required = False
        
    class Meta:
        model = Workpermit
        fields = ['Contracting_Company_Name','station_name']
        widgets = {
           
            'Contracting_Company_Name': forms.Select(attrs={'class': 'form-control'}),
            'station_name': forms.Select(attrs={'class':'form-select'}),
           
        }
        labels = {        
            'Contracting_Company_Name' : 'Vendor',
            'station_name' : 'Station' 
        }
        
class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['nature_of_injury', 'user']
        widgets = {
            'nature_of_injury': forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super(IncidentForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()  # Hide the user field
        self.fields['user'].initial = self.initial.get('user')  # Set the initial value for the user field


class GatePassForm(forms.ModelForm):

    def clean_Contact_Details(self):
        phone_number = self.cleaned_data.get('Contact_Details')
        #phone_number_str = str(phone_number)
        if len(phone_number) != 10:
            raise ValidationError('Phone number must be 10 digits long.')
        return phone_number
    
    def clean_Iqama_Number(self):
        Iqama_Number = self.cleaned_data.get('Iqama_Number')
        #Iqama_Number_str = str(Iqama_Number)
        if len(Iqama_Number) != 10:
            raise ValidationError('Iqama/NationalID number must be 10 digits long.')
        return Iqama_Number
    
    class Meta:
        model = GatePassModel
        fields = '__all__'
        exclude = ['Created_time','user','Return_date']
        widgets = {
            'Return_status': forms.RadioSelect(choices=[(1, 'Returnable'), (2, 'Non-Returnable')]),
            'Reason': forms.Textarea(attrs={'rows': 2}) ,
            'Item_Description' : forms.Textarea(attrs={'rows': 2}),
            'Issue_Date': forms.DateInput(attrs={'type': 'date','readonly': 'readonly'}),
            'phone_number' :forms.TextInput(attrs={'type': 'number'}),
            'Iqama_Number' :forms.TextInput(attrs={'type': 'number'}),
            'image1': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            
           
        }
        help_texts = {
            'Contact_Details': ' Ex:0580656544',
            'Vehicle_Plate_Number' : 'Ex: GND 1969'
            
        }
        labels={
            'Return_status': 'Item Return Status'
        }
        error_messages = {
        'image1': {
            'invalid_image': "Please upload a valid image file with following extensions ('.jpg', '.jpeg', '.png', '.gif')",
            'invalid_format': "The file format is not supported. Please upload an image file.",
        },
    }

class GatepassItemForm(forms.ModelForm):

    class Meta:
        model = Gatepass_Items_Model
        fields = '__all__'
        exclude = ['GatePass']
        widgets = {
        'Remarks': forms.Textarea(attrs={'rows': 1})
        }
        labels={
            'Description': 'Item Description'
        }
class WorkerForm(forms.ModelForm):


    def clean_Iqama_Number(self):
        Iqama_Number = self.cleaned_data['Iqama_Number']
        if Workers.objects.filter(Iqama_Number=Iqama_Number).exists():
            raise forms.ValidationError('IQAMA ID exists.')
        
        if len(Iqama_Number) != 10:
            raise ValidationError('Iqama/NationalID number must be 10 digits long.')
        
        return Iqama_Number
    
    def clean_Employee_name(self):
        Employee_name = self.cleaned_data['Employee_name']
        if not Employee_name.isupper():
                Employee_name = Employee_name.upper()
        if Workers.objects.filter(Employee_name=Employee_name).exists():
            raise forms.ValidationError('Employee Name exists.') 
        
        return Employee_name
    
    """ def clean_upload_Iqama(self):
        upload_Iqama = self.cleaned_data.get('upload_Iqama')
        if upload_Iqama:
            if not upload_Iqama.name.endswith('.pdf'):
                raise forms.ValidationError("Please upload only PDF files.")
        return upload_Iqama """
    
    class Meta:
        model = Workers
        fields = '__all__'


        widgets = {
            
            'upload_Iqama': forms.FileInput(attrs={'class': 'form-control',}),
            
        }
        labels = {
            
            'upload_Iqama' : 'Upload Iqama Copy'
    
        }
      

class ContractorForm(forms.ModelForm):
    
    
    def clean_Company_Name(self):
        Company_Name = self.cleaned_data['Company_Name']
        if not Company_Name.isupper():
                Company_Name = Company_Name.upper()
        if Contractor.objects.filter(Company_Name=Company_Name).exists():
            raise forms.ValidationError('Company Name exists.') 
        return Company_Name 


    class Meta:
        model = Contractor
        fields = '__all__'


class Fa_CategoryForm(forms.ModelForm):
    
    
    class Meta:
        model = Fa_Category
        fields = '__all__'
        widgets={
            'description' : forms.Textarea(attrs={'rows': 2}),
        }

class Fa_SubCategoryForm(forms.ModelForm):
    
    
    class Meta:
        model = Fa_SubCategory
        fields = '__all__'
        widgets={
            'description' : forms.Textarea(attrs={'rows': 2}),
        }
 
        
class Fa_ContractForm(forms.ModelForm):
    
    
    class Meta:
        model = Fa_Contract
        exclude = ['PO_copy']
        fields = '__all__'
        widgets={
             'start_date': forms.DateInput(attrs={'class': 'form-control','type': 'date',}),
            'end_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'contract_copy': forms.FileInput(attrs={'class': 'form-control'}),
            'po': forms.FileInput(attrs={'class': 'form-control'}),
            'Remarks' : forms.Textarea(attrs={'rows': 2}),
            
        }

class Fa_FileuploadForm(forms.ModelForm):
    
    
    class Meta:
        model = Fa_ContractFile
        fields = ['filename','file']
        #exclude = ['contract','Created_By']
        widgets={
             
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'Remarks': forms.Textarea(attrs={'class': 'form-control','rows': 2}),
        }
        labels={
            'file':'Upload File'
        }
 
        
class Fa_PMForm(forms.ModelForm):
    
    
    
    class Meta:
        model = PreventiveMaintenance
        fields = '__all__'
        exclude=['Created_By','work_order','uploaded_at','pm_datetime','next_pm_date','email_sent']
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude contracts with status == 2
        self.fields['contract'].queryset = Fa_Contract.objects.exclude(status=2)


    def clean_contract(self):
        contract = self.cleaned_data.get('contract')
            
        if contract.contract_reference_number =="NA":
            raise forms.ValidationError("Contract cannot be 'NA'. Please select a valid contract.")
        return contract
    
    def clean(self):
        # First call the parent clean method, which ensures individual field validation
        cleaned_data = super().clean()

        # Extracting data from cleaned_data
        contract = cleaned_data.get('contract')
        details = cleaned_data.get('details')
        station_name = cleaned_data.get('station_name')
        today_date = timezone.now().date()

        # Perform the duplicate check
        if PreventiveMaintenance.objects.filter(
        contract=contract,
        details=details,
        station_name=station_name,
        uploaded_at=today_date

        ).exists():
        # If duplicates are found, raise a ValidationError
            raise ValidationError("Another PM with the same scope of work already existing.")

        # Always return the cleaned_data
        return cleaned_data

    
    

        

    

        
 
            

class Fa_CMForm(forms.ModelForm):
    
    
    class Meta:
        model = CorrectiveMaintenance
        fields = '__all__'
        exclude=['Created_By','work_order','uploaded_at']
        widgets={
            'work_order': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude contracts with status == 2
        self.fields['contract'].queryset = Fa_Contract.objects.exclude(status=2)

    def clean_contractor(self):
        contractor = self.cleaned_data.get('contractor')
        if contractor.Company_Name =="NA":
            raise forms.ValidationError("Contractor cannot be 'NA'. Please select a valid contractor.")
        return contractor
    
    def clean(self):
        # First call the parent clean method, which ensures individual field validation
            cleaned_data = super().clean()

            # Extracting data from cleaned_data
            contract = cleaned_data.get('contract')
            Scope_of_Work = cleaned_data.get('Scope_of_Work')
            category = cleaned_data.get('category')
            subcategory= cleaned_data.get('subcategory')
            if subcategory:
                subcategories = cleaned_data.get('subcategory').all()
            else:
                subcategories=[]
            station_name = cleaned_data.get('station_name')
            today_date = timezone.now().date()
        # Perform the duplicate check
            duplicate_cm = CorrectiveMaintenance.objects.filter(
                contract=contract,
                Scope_of_Work=Scope_of_Work,
                station_name=station_name,
                category=category,
                uploaded_at=today_date,
            ).distinct()
            for cm in duplicate_cm:
                if set(cm.subcategory.all()) == set(subcategories):
                    raise ValidationError("Another CM with the same scope of work already existing.")
            return cleaned_data
    


class Fa_NewWorkForm(forms.ModelForm):
    
    
    class Meta:
        model = NewMaintanence
        fields = '__all__'
        exclude=['created_by','work_order','uploaded_at']
        widgets = {
            'scope_of_work': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter scope of work'}),
            'contract': forms.Select(attrs={'class': 'form-control'}),  # Custom widget for contract field
            'contractor': forms.Select(attrs={'class': 'form-control'}),  # Custom widget for contractor
            'category': forms.Select(attrs={'class': 'form-control'}),
            'station_name': forms.Select(attrs={'class': 'form-control'}),
            'purchase_order': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter purchase order'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
        }
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude contracts with status == 2
        self.fields['contract'].queryset = Fa_Contract.objects.exclude(status=2)
        # Optional: Add a custom label for certain fields, or set placeholder text
        self.fields['subcategory'].label = "Subcategories"
        self.fields['purchase_order'].help_text = "Please enter the associated purchase order number."

    def clean_contractor(self):
        contractor = self.cleaned_data.get('contractor')
        if contractor.Company_Name =="NA":
            raise forms.ValidationError("Contractor cannot be 'NA'. Please select a valid contractor.")
        return contractor


class Fa_PMFileuploadForm(forms.ModelForm):
    
    
    class Meta:
        model = Fa_PM_ContractFile
        fields = ['filename','file']
        #exclude = ['contract','Created_By']
        widgets={
             
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels={
            'file':'Upload File'
        }

class Fa_CMFileuploadForm(forms.ModelForm):
    
    
    class Meta:
        model = Fa_CM_ContractFile
        fields = ['filename','file']
        #exclude = ['contract','Created_By']
        widgets={
             
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels={
            'file':'Upload File'
        }
        
class Fa_NewFileuploadForm(forms.ModelForm):
    
    
    class Meta:
        model = Fa_New_ContractFile
        fields = ['filename','file']
        #exclude = ['contract','Created_By']
        widgets={
             
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels={
            'file':'Upload File'
        }



class NewCommentForm(forms.ModelForm):
    class Meta:
        model = New_Comment
        fields = ['text']
        widgets={
             'text': forms.Textarea(attrs={'rows': 2}) ,
        }
        
class PMCommentForm(forms.ModelForm):
    class Meta:
        model = PM_Comment
        fields = ['text']
        widgets={
             'text': forms.Textarea(attrs={'rows': 2}) ,
        }

class CMCommentForm(forms.ModelForm):
    class Meta:
        model = CM_Comment
        fields = ['text']
        widgets={
             'text': forms.Textarea(attrs={'rows': 2}) ,
        }


class PM_WorkPermitForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.obj = kwargs.pop('obj', None)
        super(PM_WorkPermitForm, self).__init__(*args, **kwargs)
        self.fields['workers'].queryset = Workers.objects.all().annotate(Employee_nam=Concat('Employee_name', Value(' '), 'Iqama_Number'))

        if self.obj:
            # Set initial values based on `obj`
            self.fields['work_order'].initial = self.obj.work_order
            self.fields['station_name'].initial = self.obj.station_name
            self.fields['station_name'].disabled = True
            self.fields['Contracting_Company_Name'].initial = self.obj.contract.contractor
            self.fields['Contracting_Company_Name'].disabled = True
            self.fields['Description'].initial = self.obj.details
            # Assuming `Created_By` and `uploaded_at` should be handled similarly
            
        

    class Meta:
        model = Workpermit
        fields = '__all__'
        exclude = ['Created_time','Contractor_Name','upload_Iqama']
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control','type': 'date',}),
            'end_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'created_date': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'Phone_number': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '1'}),
            'Iqama_number': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '1'}),
            'Description': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'cols': 40,'readonly': 'readonly'}),
            'Additional_notes': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'cols': 40}),
            'Tools': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'cols': 40}),
            'upload_Iqama': forms.FileInput(attrs={'class': 'form-control'}),
            'workers': forms.SelectMultiple(attrs={'class': 'form-control','id':'id_workers'}),
            'Contracting_Company_Name': forms.Select(attrs={'class': 'form-control','readonly': 'readonly'}),
            'work_order': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'station_name': forms.Select(attrs={'class':'form-select','readonly': 'readonly'}),
            'Staff_in_charge': forms.TextInput(attrs={'class': 'form-control'}),
            'Employee_Count': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '1'}),

            
            
            # Replace 'your_date_field_name' with the actual name of your date field in the model
            # 'attrs': {'type': 'date'} specifies the use of a date picker in HTML5
        }
        labels = {
            'Description': 'Scope of Work',
            'Contractor_Name': 'Company Name',
            'Staff_in_charge': 'Staff In Charge',
            'Contractor_Name' : 'Vendor Company Name',
            'Staff_in_charge' : 'Vendor Staff In charge',
            'upload_Iqama' : 'Upload Iqama Copy',
            'work_order' : 'work order'
    
        }
        validators = {
            'upload_Iqama': [FileExtensionValidator(allowed_extensions=['pdf'], message='Please upload only PDF files.')]
        }

class CM_WorkPermitForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.obj = kwargs.pop('obj', None)
        super(CM_WorkPermitForm, self).__init__(*args, **kwargs)
        self.fields['workers'].queryset = Workers.objects.all().annotate(Employee_nam=Concat('Employee_name', Value(' '), 'Iqama_Number'))

        if self.obj:
            # Set initial values based on `obj`
            self.fields['work_order'].initial = self.obj.work_order
            self.fields['station_name'].initial = self.obj.station_name
            self.fields['station_name'].disabled = True
            self.fields['Contracting_Company_Name'].initial = self.obj.contractor
            self.fields['Contracting_Company_Name'].disabled = True
            self.fields['Description'].initial = self.obj.Scope_of_Work
            # Assuming `Created_By` and `uploaded_at` should be handled similarly
            
        

    class Meta:
        model = Workpermit
        fields = '__all__'
        exclude = ['Created_time','Contractor_Name','upload_Iqama']
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control','type': 'date',}),
            'end_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'created_date': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'Phone_number': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '1'}),
            'Iqama_number': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '1'}),
            'Description': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'cols': 40,'readonly': 'readonly'}),
            'Additional_notes': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'cols': 40}),
            'Tools': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'cols': 40}),
            'upload_Iqama': forms.FileInput(attrs={'class': 'form-control'}),
            'workers': forms.SelectMultiple(attrs={'class': 'form-control','id':'id_workers'}),
            'Contracting_Company_Name': forms.Select(attrs={'class': 'form-control','readonly': 'readonly'}),
            'work_order': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'station_name': forms.Select(attrs={'class':'form-select','readonly': 'readonly'}),
            'Staff_in_charge': forms.TextInput(attrs={'class': 'form-control'}),
            'Employee_Count': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '1'}),

            
            
            # Replace 'your_date_field_name' with the actual name of your date field in the model
            # 'attrs': {'type': 'date'} specifies the use of a date picker in HTML5
        }
        labels = {
            'Description': 'Scope of Work',
            'Contractor_Name': 'Company Name',
            'Staff_in_charge': 'Staff In Charge',
            'Contractor_Name' : 'Vendor Company Name',
            'Staff_in_charge' : 'Vendor Staff In charge',
            'upload_Iqama' : 'Upload Iqama Copy',
            'work_order' : 'work order'
    
        }
        validators = {
            'upload_Iqama': [FileExtensionValidator(allowed_extensions=['pdf'], message='Please upload only PDF files.')]
        }
        
###

class New_WorkPermitForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.obj = kwargs.pop('obj', None)
        super(New_WorkPermitForm, self).__init__(*args, **kwargs)
        self.fields['workers'].queryset = Workers.objects.all().annotate(Employee_nam=Concat('Employee_name', Value(' '), 'Iqama_Number'))

        if self.obj:
            # Set initial values based on `obj`
            self.fields['work_order'].initial = self.obj.work_order
            self.fields['station_name'].initial = self.obj.station_name
            self.fields['station_name'].disabled = True
            self.fields['Contracting_Company_Name'].initial = self.obj.contractor
            self.fields['Contracting_Company_Name'].disabled = True
            self.fields['Description'].initial = self.obj.scope_of_work
            # Assuming `Created_By` and `uploaded_at` should be handled similarly
            
        

    class Meta:
        model = Workpermit
        fields = '__all__'
        exclude = ['Created_time','Contractor_Name','upload_Iqama']
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control','type': 'date',}),
            'end_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'created_date': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'Phone_number': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '1'}),
            'Iqama_number': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '1'}),
            'Description': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'cols': 40,'readonly': 'readonly'}),
            'Additional_notes': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'cols': 40}),
            'Tools': forms.Textarea(attrs={'class': 'form-control','rows': 3, 'cols': 40}),
            'upload_Iqama': forms.FileInput(attrs={'class': 'form-control'}),
            'workers': forms.SelectMultiple(attrs={'class': 'form-control','id':'id_workers'}),
            'Contracting_Company_Name': forms.Select(attrs={'class': 'form-control','readonly': 'readonly'}),
            'work_order': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'station_name': forms.Select(attrs={'class':'form-select','readonly': 'readonly'}),
            'Staff_in_charge': forms.TextInput(attrs={'class': 'form-control'}),
            'Employee_Count': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': '1'}),

            
            
            # Replace 'your_date_field_name' with the actual name of your date field in the model
            # 'attrs': {'type': 'date'} specifies the use of a date picker in HTML5
        }
        labels = {
            'Description': 'Scope of Work',
            'Contractor_Name': 'Company Name',
            'Staff_in_charge': 'Staff In Charge',
            'Contractor_Name' : 'Vendor Company Name',
            'Staff_in_charge' : 'Vendor Staff In charge',
            'upload_Iqama' : 'Upload Iqama Copy',
            'work_order' : 'work order'
    
        }
        validators = {
            'upload_Iqama': [FileExtensionValidator(allowed_extensions=['pdf'], message='Please upload only PDF files.')]
        }
        