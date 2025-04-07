
from datetime import datetime
from django import forms
from django.shortcuts import get_object_or_404
from accounts.models import CustomUser
from itassets.models import CCTV, It_Brand, It_Category, It_Device_Status, It_Mobile, It_Model, It_Prodcuts, ItAssetAllocation, MaintenanceRequest
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import TabHolder, Tab
from formtools.wizard.views import WizardView
from crispy_forms.layout import HTML
from django.utils import timezone

class ItProdForm(forms.ModelForm):
    
    class Meta:
        model = It_Prodcuts
        fields = ['status']
        widgets = {
            'status': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(ItProdForm, self).__init__(*args, **kwargs)
        self.fields['status'].queryset = It_Device_Status.objects.all()
        
        
class ItProductForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['station_name'].empty_label = 'select station'
        self.fields['created_date'].initial = timezone.now().date()
        
    
    def clean_serial_number(self):  
       
        serial_number = self.cleaned_data['serial_number']
        instance = self.instance
        if instance.pk is None:
            existing_records = It_Prodcuts.objects.filter(serial_number=serial_number)
       
            if existing_records.exists(): 
                raise forms.ValidationError("Serial Number Exists")  
        return serial_number 
    
    class Meta:
        model = It_Prodcuts
        fields = '__all__'
        exclude = ['allocation_status']
        widgets = {
            
            'brand':forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
            'category':forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
            'model': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'serial_number': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'Asset_tag': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'supplier': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'warranty_start_date': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'warranty_end_date': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'created_date': forms.TextInput(attrs={'readonly': 'readonly','class':'form-control'}),
            'po_number': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'station_name':forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
            'processor': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'ram': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'harddisk': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'operating_system': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
            'asset_remarks': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
             'price': forms.TextInput(attrs={'type': 'number', 'class':'form-control','step': '0.01'}),
             'device_model': forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
           
            
            
        }
        labels = {
            'brand': 'Brand',
            'category': 'Category',
            'model': 'Model',
            'serial_number': 'Serial Number',
            'Asset_tag': 'Asset Tag',
            'supplier': 'Supplier',
            'warranty_start_date': 'Warranty Start Date',
            'warranty_end_date': 'Warranty End Date',
            'po_number': 'PO Number',
            'processor': 'Processor',
            'ram': 'Memmory',
            'harddisk': 'Hardisk Capacity',
            'operating_system': 'Operating System',
            'status': 'Product Condition',
            'station_name': 'Station Name',
            'file' : 'Upload files',
            'image' : 'Upload Image',
            'asset_remarks': 'Remarks',
            'location' : 'Location',
            'price' : 'Price',
            'created_date' :'Created Date',
             'device_model' :'Model',
    
        }
class ItProductFormEdit(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        maintanence_obj_initial = kwargs.get('initial', {}).get('maintanence_obj')  
       
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        self.fields['station_name'].empty_label = 'select station'
        self.fields['created_date'].initial = timezone.now().date()
        
        if instance :
            if maintanence_obj_initial is not None:
                maint_obj_status = maintanence_obj_initial.status if maintanence_obj_initial else None

                if maint_obj_status in ['1', '2']:
                    self.fields['status'].widget.attrs['readonly'] = True
                   
     
        
    
    def clean_serial_number(self):  
       
        serial_number = self.cleaned_data['serial_number']
        instance = self.instance
        if instance.pk is None:
            existing_records = It_Prodcuts.objects.filter(serial_number=serial_number)
       
            if existing_records.exists(): 
                raise forms.ValidationError("Serial Number Exists")  
        return serial_number 
    
    class Meta:
        model = It_Prodcuts
        fields = '__all__'
        exclude = []
        widgets = {
            
            'brand':forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
            'category':forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
            'model': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'serial_number': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'Asset_tag': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'supplier': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'warranty_start_date': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'warranty_end_date': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'created_date': forms.TextInput(attrs={'readonly': 'readonly','class':'form-control'}),
            'po_number': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'station_name':forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
            'processor': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'ram': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'harddisk': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'operating_system': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
            'asset_remarks': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
             'price': forms.TextInput(attrs={'type': 'number', 'class':'form-control','step': '0.01'}),
             'device_model': forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
             'allocation_status': forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
           
            
            
        }
        labels = {
            'brand': 'Brand',
            'category': 'Category',
            'model': 'Model',
            'serial_number': 'Serial Number',
            'Asset_tag': 'Asset Tag',
            'supplier': 'Supplier',
            'warranty_start_date': 'Warranty Start Date',
            'warranty_end_date': 'Warranty End Date',
            'po_number': 'PO Number',
            'processor': 'Processor',
            'ram': 'Memmory',
            'harddisk': 'Hardisk Capacity',
            'operating_system': 'Operating System',
            'status': 'Product Condition',
            'station_name': 'Station Name',
            'file' : 'Upload files',
            'image' : 'Upload Image',
            'asset_remarks': 'Remarks',
            'location' : 'Location',
            'price' : 'Price',
            'created_date' :'Created Date',
             'device_model' :'Model',
    
        }
    
        
class PersonDetailForm(forms.ModelForm):
    class Meta:
        model = It_Prodcuts
        fields = '__all__'
        widgets = {
            'warranty_start_date': forms.DateInput(attrs={'type': 'date',}),
            'warranty_end_date': forms.DateInput(attrs={'type': 'date'}),
            'created_date': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
        labels = {
            'brand': 'Brand',
            'category': 'Category',
            'model': 'Model',
            'serial_number': 'Serial Number',
            'Asset_tag': 'Asset Tag',
            'supplier': 'Supplier',
            'warranty_start_date': 'Warranty Start Date',
            'warranty_end_date': 'Warranty End Date',
            'po_number': 'PO Number',
            'processor': 'Processor',
            'ram': 'Memmory',
            'harddisk': 'Hardisk Capacity',
            'operating_system': 'Operating System',
            'status': 'Product Condition',
            'allocation_status': 'Availability',
            'station_name': 'Station Name',
            'file' : 'Upload files'
    
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TabHolder(
                Tab('ASSET DETAILS',
                    'brand',
                    'category',
                    'model',
                    'serial_number',
                    'Asset_tag',
                    'station_name',
                    'file',
                    'image',
                    HTML('<a id="vendor" class="btn btn-primary btn-block" href="#vendor-info" data-toggle="tab">NEXT</a>')
                     
                    
                    # Add a comma here
                     
                ),
                Tab('VENDOR INFO',
                    'supplier',
                    'warranty_start_date',
                    'warranty_end_date',
                    'po_number',
                    'created_date',
                    HTML('<a id="configure" class="btn btn-primary btn-block" href="#configuration" data-toggle="tab">NEXT</a>')
                     
                ),
                Tab('CONFIGURATION',
                    'processor',
                    'ram',
                    'harddisk',
                    'operating_system',
                    'status',
                    'allocation_status',
                    HTML('<button type="submit" class="btn btn-primary btn-block" name="wizard_goto_step" value="{{ wizard.steps.last }}">Submit</button>')
                )
            ),
        )
        self.fields['brand'].widget.attrs['novalidate'] = True
        self.fields['model'].widget.attrs['novalidate'] = True
        self.fields['created_date'].widget.attrs['novalidate'] = True
        #self.fields['created_date'].initial = date.today()
        
class FormStepOne(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms. CharField(max_length=100)
    email = forms.EmailField()
class FormStepTwo(forms.Form):
    job = forms.CharField(max_length=100)
    salary = forms.CharField(max_length=100)
    job_description = forms.CharField(widget=forms.Textarea)
    
    
    
class ItProductsform1(forms.ModelForm):
    
    def clean_serial_number(self):
        serial_number = self.cleaned_data['serial_number']
        instance = self.instance
        

        # Check if the instance is new or the serial number is being changed
        if instance.pk is None or instance.serial_number != serial_number:
            existing_records = It_Prodcuts.objects.filter(serial_number=serial_number)

            if existing_records.exists():
                raise forms.ValidationError("Serial Number Exists")

        return serial_number
    
    class Meta:
        model = It_Prodcuts
        fields = ['brand', 'category', 'model', 'serial_number','Asset_tag','station_name']
        labels = {
            'brand': 'Brand',
            'category': 'Category',
            'model': 'Model',
            'serial_number': 'Serial Number',
            'Asset_tag': 'Asset Tag',
            'station_name': 'Station Name',
            
        }
class ItProductsform2(forms.ModelForm):
    class Meta:
        model = It_Prodcuts
        fields = ['supplier', 'warranty_start_date', 'warranty_end_date', 'po_number']
        widgets = {
            'warranty_start_date': forms.DateInput(attrs={'type': 'date',}),
            'warranty_end_date': forms.DateInput(attrs={'type': 'date'}),
            'created_date': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
        labels = {
            'supplier': 'Supplier',
            'warranty_start_date': 'Warranty Start Date',
            'warranty_end_date': 'Warranty End Date',
            'po_number': 'PO Number',
            
        }
class ItProductsform3(forms.ModelForm):
    class Meta:
        model = It_Prodcuts
        fields = ['processor', 'ram', 'harddisk', 'operating_system','status']
        labels = {
            'processor': 'Processor',
            'ram': 'Memmory',
            'harddisk': 'Hardisk Capacity',
            'operating_system': 'Operating System',
            'status': 'Product Condition',
           
        }
        
class ItAssetAllocationForm(forms.ModelForm):
    serial_number = forms.CharField(max_length=100)
    
    class Meta:
        model = ItAssetAllocation
        fields = ['user','allocation_date']
        

        
    def __init__(self,testid, *args, **kwargs):
        super(ItAssetAllocationForm, self).__init__(*args, **kwargs)
        Asset_details = It_Prodcuts.objects.get(id=testid)
    
        self.fields['user'].widget.attrs.update({'id': 'allocate_userid'})
        self.fields['serial_number'].initial = Asset_details
        self.fields['serial_number'].widget.attrs.update({'id': 'allocate_serial1'})
        self.fields['serial_number'].widget.attrs.update({'readonly': 'readonly'})
        self.fields['allocation_date'].widget.attrs.update({'readonly': 'readonly'})
        self.fields['allocation_date'].initial = timezone.now()
        
     
        
class ItAssetHandOverForm(forms.Form):
   
    allocation_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'readonly': 'readonly'}))
    serial_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
   
    def __init__(self,asset_id, *args, **kwargs):
        super(ItAssetHandOverForm, self).__init__(*args, **kwargs)
        users = CustomUser.objects.all()
        Asset_details = It_Prodcuts.objects.get(id=asset_id)
        choices = [(None, 'Select User')]
        choices +=  [(user.id, user.employee_id) for user in users]
        # Create the dropdown field
        self.fields['user'] = forms.ChoiceField(choices=choices)
        self.fields['user'].label = "Select User"
        self.fields['user'].widget.attrs.update({'id': 'id_user'})
        self.fields['serial_number'].initial = Asset_details
        self.fields['allocation_date'].initial = timezone.now()
       
class ITBrandsForm(forms.ModelForm):

        def clean_brand(self):
            brand = self.cleaned_data.get('brand')
    
                # Capitalize the brand name
            if not brand.isupper():
                brand = brand.upper()
            if It_Brand.objects.filter(brand=brand).exists():
                raise forms.ValidationError("Brand already exists.")
            return brand


        class Meta:
            model = It_Brand
            fields = '__all__'

            labels={
                'brand': 'Brand',
            }


class ITCategoryForm(forms.ModelForm):

        def clean_category(self):
            category = self.cleaned_data.get('category')
            if not category.isupper():
                category = category.upper()
            if It_Category.objects.filter(category=category).exists():
                raise forms.ValidationError("category already exists.")
            return category


        class Meta:
            model = It_Category
            fields = '__all__'


class ITModelForm(forms.ModelForm):

   
        class Meta:
            model = It_Model
            fields = ['category','brand','model_name']


class ITMobilePhoneForm(forms.ModelForm):
    def clean_imei(self):
            imei = self.cleaned_data.get('imei')
    
                # Capitalize the brand name
            if not imei:
                raise forms.ValidationError("IMEI number required.")
            if It_Mobile.objects.filter(imei=imei).exists():
                raise forms.ValidationError("IMEI already exists.")
            return imei
    class Meta:
        model = It_Mobile
        exclude = ['Itproduct']
        fields = '__all__'
        widgets={
            'imei': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
        }

class ITCCTVForm(forms.ModelForm):

    def clean_ip_address(self):
            ip_address = self.cleaned_data.get('ip_address')
    
             
            if not ip_address:
                raise forms.ValidationError("IP address cannot be blank.")
            if self.instance.pk:
                # Get the primary key of the current instance
                current_instance_pk = self.instance.pk

                # Check if there is any other instance with the same IP address
                if CCTV.objects.filter(ip_address=ip_address).exclude(pk=current_instance_pk).exists():
                    raise forms.ValidationError("IP address already exists.")
            else:
                # For new instances, simply check if the IP address already exists
                if CCTV.objects.filter(ip_address=ip_address).exists():
                    raise forms.ValidationError("IP address already exists.")
        
            return ip_address
    class Meta:
        model = CCTV
        exclude = ['it_product']
        fields = '__all__'
        widgets={
            'ip_address': forms.TextInput(attrs={'type': 'text','class':'form-control'}),
        }


class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['it_product','description']
        
        widgets={
            'it_product':forms.Select(attrs={'class': 'col-12 col-md-8 col-lg-8', 'type': 'select'}),
            'description' : forms.Textarea(attrs={'rows':'2','class': 'col-12 col-md-8 col-lg-8'}),
           
        }

    def clean(self):
        cleaned_data = super().clean()
        Serial_Number=cleaned_data.get('it_product')
        
        
        if Serial_Number is None:
                 raise ValidationError("IT product is required")
                
        else:
            
            Serial_Number_id=Serial_Number.id
        
        if MaintenanceRequest.objects.filter(it_product=Serial_Number_id).exists():
            Maint_Req_Obj=MaintenanceRequest.objects.filter(it_product=Serial_Number_id).last()
            Job_Status = Maint_Req_Obj.status
            if Job_Status in ["1", "2"]:
                raise ValidationError("Another Maintanence Request In Progress for the asset.")

        return cleaned_data
    
class MaintenanceEditForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['description','Vendor','is_under_warranty','Warranty_type','completion_date','status','Payment_Mode','po_number','amount','is_Device_Repalced','Replaced_Device_Serial_Number','Remarks','file']
        exclude =['request_date']
        
        widgets={
            'completion_date': forms.DateInput(attrs={'type': 'date'}),
            'description' : forms.Textarea(attrs={'rows':'2'}),
             'file': forms.FileInput(attrs={'class': 'form-control'}),
           
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
       
       
        self.fields['it_product_hidden'] = forms.ModelChoiceField(queryset=It_Prodcuts.objects.all(), widget=forms.HiddenInput, required=False)

        # Set the initial value of the hidden field to the instance of it_product
        self.initial['it_product_hidden'] = self.instance.it_product if self.instance else None

    def clean(self):
        cleaned_data = super().clean()
        is_under_warranty = cleaned_data.get('is_under_warranty')
        po_number = cleaned_data.get('po_number')
        status= cleaned_data.get('status')
        Payment_Mode=cleaned_data.get('Payment_Mode')
        Warranty_type=cleaned_data.get('Warranty_type')
        amount=cleaned_data.get('amount')
        Serial_Number=cleaned_data.get('it_product_hidden')
        file = cleaned_data.get('file')
        is_Device_Repalced=cleaned_data.get('is_Device_Repalced')
        Replaced_Device_Serial_Number=cleaned_data.get('Replaced_Device_Serial_Number')
        Serial_Number_id=Serial_Number
        if file:
            print('file')
            max_size_kb = 5 * 1024  # 5MB in KB
            if file.size > max_size_kb * 1024:
                raise ValidationError(f"The maximum file size that can be uploaded is {max_size_kb}KB")
            
        
            
          
        if not self.instance.pk:
            
            if MaintenanceRequest.objects.filter(it_product=Serial_Number_id).exists():
                Maint_Req_Obj=MaintenanceRequest.objects.filter(it_product=Serial_Number_id).last()
                Job_Status = Maint_Req_Obj.status
                if Job_Status in ["1", "2"]:
                    raise ValidationError("Another Maintanence Request In Progress for the asset.change the status to completed.")
            
        if status in ["3"]:
            if is_under_warranty is None:
                self.add_error('is_under_warranty', 'Cannot be empty')

            if Payment_Mode is None:
                self.add_error('Payment_Mode', 'Select Payment mode')

            if is_Device_Repalced is None:
                self.add_error('is_Device_Repalced', 'Select status')
            else:
                if is_Device_Repalced :
                    if Replaced_Device_Serial_Number is None:
                        self.add_error('Replaced_Device_Serial_Number', 'Add the new device serial number')

                
            if not is_under_warranty:  
                if Payment_Mode == "1" and not po_number:
                    self.add_error('po_number', 'PO is required if payment mode is PO and is out of warranty.')
                else:
                    if Payment_Mode == "2" and not amount:
                        self.add_error('amount', 'Amount is required if payment mode is Cash and is out of warranty.')
            else:
                if Warranty_type is None:
                    self.add_error('Warranty_type', 'Cannot be empty')
                else:
                    if Warranty_type in ["2"]:
                        if Payment_Mode == "1" and not po_number:
                            self.add_error('po_number', 'PO is required if payment mode is PO  in partial warranty.')
                        else:
                            if Payment_Mode == "2" and not amount:
                                self.add_error('amount', 'Amount is required if payment mode is Cash  in partial warranty.')
                    else:
                        if Payment_Mode in ['1','2']:
                            self.add_error('Payment_Mode', 'Payment Mode cannot be cash or PO if warranty coverage is full.Please select NA')






            

        return cleaned_data