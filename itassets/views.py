#from datetime import datetime
import os
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
import pandas as pd
from tablib import Dataset
from django.contrib import messages
from django.db.models import Q
from accounts.models import CustomUser
from itassets.models import It_Prodcuts
from django.views.generic.edit import UpdateView
from .forms import ITBrandsForm, ITCCTVForm, ITCategoryForm, ITMobilePhoneForm, ITModelForm, ItAssetAllocationForm, ItAssetHandOverForm, ItProdForm, ItProductForm, ItProductFormEdit, ItProductsform1, ItProductsform2, ItProductsform3, MaintenanceEditForm, MaintenanceRequestForm, PersonDetailForm
from .resources import It_ProdcutsResources
from formtools.wizard.views import SessionWizardView
from .forms import FormStepOne, FormStepTwo
from .models import Allocation_status, It_Device_Status, It_Model, It_Prodcuts, ItAssetAllocation, Maint_Request_history, MaintenanceRequest
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseServerError
from xhtml2pdf import pisa
from io import BytesIO, StringIO
from django.template.loader import get_template
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from simple_history.models import HistoricalRecords
import threading
from django.dispatch import Signal
from django.contrib.auth.decorators import login_required
import ast






# Create your views here.

def choices_view(request):
    if request.method == 'POST':
        form = ItProdForm(request.POST)
        if form.is_valid():
            selected_choices = form.cleaned_data['status']
            print(selected_choices)  # Print the selected choices
            form.save()  # Save the form if needed
    else:
        form = ItProdForm()
    return render(request, 'itassets/import.html', {'form': form})


""" def It_Product_Upload(request):
    if request.method == 'POST':
        person_resource = It_ProdcutsResources()
        new_persons = request.FILES['myfile']
        df = pd.read_excel(new_persons)
        
    
        dataset = Dataset().load(df)
        
        # Call the import_data hook and pass the tablib dataset
        result = person_resource.import_data(dataset,\
             dry_run=True, raise_errors = True)

        if not result.has_errors():
            result = person_resource.import_data(dataset, dry_run=False)
            messages.success(request,'data imported successfully')
            return redirect ('itassets:itassetdisplay')
        else:
            messages.success(request,'data imported failed due to errors')
            return redirect ('itassets:It_Product_Upload')
    #form = ChoicesForm()
    #return render(request,"itassets/import.html",{'form':form}) """
def It_Product_Upload(request):
    if request.method == 'POST':
        person_resource = It_ProdcutsResources()
        new_persons = request.FILES['myfile']
        df = pd.read_excel(new_persons)
        
    
        dataset = Dataset().load(df)
        
        # Call the import_data hook and pass the tablib dataset
        result = person_resource.import_data(dataset,\
             dry_run=True, raise_errors = True)

        if not result.has_errors():
            result = person_resource.import_data(dataset, dry_run=False)
            messages.success(request,'data imported successfully')
            return redirect ('itassets:itassetdisplay')
        else:
            messages.success(request,'data imported failed due to errors')
            return redirect ('itassets:It_Product_Upload')
    
    return render(request,"itassets/import.html")
    

def It_Product_Add(request):
    itbrandform = ITBrandsForm()
    itcategoryform = ITCategoryForm()
    if request.method == "POST":
        category_value = request.POST.get('category')

      
        form = ItProductForm(request.POST, request.FILES)


        if category_value == "20":
           
            mobile_phone_form = ITMobilePhoneForm(request.POST)
            if mobile_phone_form.is_valid() and form.is_valid():
                it_product=form.save()
                mobile_phone = mobile_phone_form.save(commit=False)
                mobile_phone.Itproduct = it_product
                mobile_phone.save()
                messages.success(request,'Product added succesfully')
                return redirect ('itassets:itassetdisplay')

            else:
               
                context = {
                    'form': form,
                    'itbrandform': itbrandform,
                    'itcategoryform': itcategoryform,
                    'itmobileform': mobile_phone_form,
                    'flag':True,
                    
                }
                return render(request, "itassets/ItAssetCreation.html", context)
            
        elif category_value == "4" :
               
                
                cctv_form = ITCCTVForm(request.POST)
               
                if cctv_form.is_valid() and form.is_valid():
                    
                    it_product=form.save()
                    cctv = cctv_form.save(commit=False)
                    cctv.it_product = it_product
                    cctv.save()
                    messages.success(request,'Product added succesfully')
                    return redirect ('itassets:itassetdisplay')

                    
                else:
                    context = {
                            'form': form,
                            'itbrandform': itbrandform,
                            'itcategoryform': itcategoryform,
                            'itcctvform': cctv_form,
                             'flag':True,
                            
                            
                        }
                    return render(request, "itassets/ItAssetCreation.html", context)
            

       
        else:
            
            if form.is_valid():
                it_product = form.save()
                messages.success(request,'Product added succesfully')
                return redirect ('itassets:itassetdisplay')
            else:
             

                context1 = {
                        'form': form,
                        }                     
                return render(request, "itassets/ItAssetCreation.html", context1)

           
            
    else:
        form = ItProductForm()
        itbrandform = ITBrandsForm()
        itcategoryform = ITCategoryForm()
        mobile_phone_form = ITMobilePhoneForm()
        cctv_form = ITCCTVForm()

        context = {
            'form': form,
            'itbrandform': itbrandform,
            'itcategoryform': itcategoryform,
            'itmobileform': mobile_phone_form,
            'itcctvform': cctv_form,
        }

        return render(request, "itassets/ItAssetCreation.html", context)


def It_Graph_Display(request):
    
    if request.method == "POST":
        print("post")
        
    else:
        ItProducts_obj = It_Prodcuts.objects.all()
        ItProducts_computers = It_Prodcuts.objects.filter(category__in=[1, 7]).count()
        ItProducts_laptop = It_Prodcuts.objects.filter(category__in=[2]).count()
        ItProducts_Printer = It_Prodcuts.objects.filter(category__in=[3]).count()
        ItProducts_SmartTV = It_Prodcuts.objects.filter(category__in=[17]).count()
        ItProducts_CCTV = It_Prodcuts.objects.filter(category__in=[4]).count()
        ItProducts_Active = It_Prodcuts.objects.filter(status__in=[1]).count()
        ItProducts_Inactive = It_Prodcuts.objects.filter(status__in=[2]).count()
        ItProducts_Damaged = It_Prodcuts.objects.filter(status__in=[4]).count()
        
        context = {
            'form' : ItProducts_obj,
            'Desktop_count' : ItProducts_computers,
            'Laptop_count' :ItProducts_laptop,
            'Printer_count' :ItProducts_Printer,
            'CCTV_count' :ItProducts_CCTV,
            'ItProducts_SmartTV' :ItProducts_SmartTV,
            'Active_asset_count' :ItProducts_Active,
            'Inactive_asset_count' :ItProducts_Inactive,
            'Damaged_asset_count' :ItProducts_Damaged,
            
        
            
        }
        return render(request,'itassets/ItAssetView.html',context)
    
my_signal = Signal()
 
def EditItAsset(request, id):
    ItProducts_obj = It_Prodcuts.objects.get(id=id)
    category =ItProducts_obj.category.id
    cctv_form = None
    Mobile_form = None
    latest_maintenance_request = MaintenanceRequest.objects.filter(it_product=ItProducts_obj).last()

    if request.method == "POST":
        
        user = request.user
        arg1 = user
        form = ItProductFormEdit(request.POST, request.FILES, instance=ItProducts_obj,initial={'maintanence_obj':latest_maintenance_request})


        if category == 20:
            
            Mobile_instance = getattr(ItProducts_obj, 'mobile_phone', None)
            mobile_phone_form = ITMobilePhoneForm(request.POST,instance=Mobile_instance)
            if mobile_phone_form.is_valid() and form.is_valid():
                it_product=form.save()
                mobile_phone = mobile_phone_form.save(commit=False)
                mobile_phone.Itproduct = it_product
                mobile_phone.save()
                messages.success(request,'Product added succesfully')
                return redirect ('itassets:itassetdisplay')

            else:
               
                context = {
                    'form': form,
                    'itmobileform': mobile_phone_form,
                    'flag':True,
                    
                }
                return render(request, "itassets/EditAsset.html", context)
        elif category == 4 :
               
                cctv_instance = getattr(ItProducts_obj, 'cctv', None)
                cctv_form = ITCCTVForm(request.POST,instance=cctv_instance)
                if cctv_form.is_valid() and form.is_valid():
                    
                    it_product=form.save()
                    cctv = cctv_form.save(commit=False)
                    cctv.it_product = it_product
                    cctv.save()
                    messages.success(request,'Product added succesfully')
                    return redirect ('itassets:itassetdisplay')
                else:
                    context={'form': form,
                     'itcctvform': cctv_form,
                     'flag':True,
                     
                     }
                    return render(request, "itassets/EditAsset.html", context)
                    

                    
        else:

       
            if form.is_valid():
                instance = form.save()
                my_signal.send( sender=It_Prodcuts,arg1=arg1,instance=instance)
                messages.success(request, 'Asset has been updated successfully.')
                return redirect('itassets:itassetdisplay')
            else:
                # If the form is not valid, render the form with the errors
                messages.error(request, 'Please fix the form errors.', extra_tags='warning')
                return render(request, 'itassets/EditAsset.html', {'form': form})
    else:
        latest_maintenance_request = MaintenanceRequest.objects.filter(it_product=ItProducts_obj).last()
        form = ItProductFormEdit(instance=ItProducts_obj,initial={'maintanence_obj':latest_maintenance_request})
       
       
        if category == 4:
            
            cctv_instance = getattr(ItProducts_obj, 'cctv', None)
            #cctv_ip_address = cctv_instance.ip_address
            cctv_form = ITCCTVForm(instance=cctv_instance)
            context={'form': form,
                     'itcctvform': cctv_form,
                     'flag':True,
                     
                     }
        elif category == 20:
            
            Mobile_instance = getattr(ItProducts_obj, 'mobile_phone', None)
            #Mobile_IMEI = Mobile_instance.imei
            
            Mobile_form = ITMobilePhoneForm(instance=Mobile_instance)
            context={'form': form,
                     'itmobileform': Mobile_form,
                     'flag':True,
                     
                     
                     }
        else:
            
            
            #form = ItProductFormEdit(instance=ItProducts_obj,initial={'maintanence_obj':latest_maintenance_request})
           
          
            context={
                'form': form,
                'maintanence_obj':latest_maintenance_request,
                
            }
            
           

    return render(request, 'itassets/EditAsset.html', context)



def view_asset_db_history(request, id):
    asset = It_Prodcuts.objects.get(id=id)
    history = asset.historical_records.all()
    
    return render(request, 'itassets/asset_history.html', {'asset': asset, 'history': history})
    
#multiform asset add
def assetaddtest(request):
    if request.method == 'POST':
        form = PersonDetailForm(request.POST,request.FILES)
        if form.is_valid():
            # Save the form data to the database
            instance = form.save()
            # You can do additional processing or redirect as needed
            return redirect('itassets:It_Asset_Display')  # Redirect to a success page
        else:
            print(form.errors)
    else:
        form = PersonDetailForm()

    return render(request, 'itassets/tab.html', {'form': form})

#test
class FormWizardView(SessionWizardView):
    template_name = "itassets/itassetadd.html"
    form_list = [FormStepOne, FormStepTwo]

    
    
    
    def done(self, form_list, **kwargs):
        formdata =[form.cleaned_data for form in form_list]
        form_step_one_data = self.get_cleaned_data_for_step('0')
        form_step_two_data = self.get_cleaned_data_for_step('1')
        
        return render(self.request, 'itassets/done.html', {
            'form_data': formdata,
            'form_step_one_data': form_step_one_data,
            'form_step_two_data': form_step_two_data,
        })
#test   
class ItProductsWizardView(SessionWizardView):
    template_name = "itassets/itassetadd.html"
    form_list = [ItProductsform1, ItProductsform2, ItProductsform3]
        
    
    def done(self, form_list, **kwargs):   
        """ for form in form_list:
            if form.is_valid():
                # Save data to the database or perform any desired actions
                # You need to adapt the following lines based on your model structure
                instance = form.save(commit=False)
                instance.save() """
       
        # Combine data from all forms
        combined_data = {}
        for form in form_list:
            combined_data.update(form.cleaned_data)
        #it_products_instance=It_Prodcuts.objects.create(**combined_data)  
        it_products_instance = It_Prodcuts(**combined_data)
        it_products_instance.save()
        
        return redirect('itassets:It_Asset_Display')
#test
class ItProductsWizardUpdateView(SessionWizardView):
    template_name = "itassets/itassetadd.html"
    form_list = [ItProductsform1, ItProductsform2, ItProductsform3]
   
   
    def get_form_kwargs(self, step=None):
        kwargs = super().get_form_kwargs(step=step)

        # Set the instance for each form based on the URL parameter
        
        kwargs['instance'] = get_object_or_404(It_Prodcuts, pk=self.kwargs['pk'])
        return kwargs
    
    def get_object(self, queryset=None):
        # Retrieve the object you want to update based on the URL parameter
        return get_object_or_404(It_Prodcuts, pk=self.kwargs['pk'])

    def get_form_initial(self, step):
        initial_data = {}
        it_products_instance = get_object_or_404(It_Prodcuts, pk=self.kwargs['pk'])
        # Load the initial data for each form step
        if step == '0':
            initial_data.update({
            'brand': it_products_instance.brand.id,
            'category': it_products_instance.category,
            'model': it_products_instance.model,
            'serial_number': it_products_instance.serial_number,
            'Asset_tag': it_products_instance.Asset_tag,
            'station_name': it_products_instance.station_name,
            
        })
            return initial_data
        elif step == '1':
            return self.get_object().__dict__
        elif step == '2':
            initial_data.update({
            'processor': it_products_instance.processor,
            'ram': it_products_instance.ram,
            'harddisk': it_products_instance.harddisk,
            'operating_system': it_products_instance.operating_system,
            'status': it_products_instance.status,
            
        })
            
            return initial_data
        else:
            return self.initial_dict.get(step, {})

 

    def done(self, form_list, **kwargs):
        # Combine data from all forms
        combined_data = {}
        for form in form_list:
            combined_data.update(form.cleaned_data)

        # Update the existing It_Prodcuts instance with the combined data
        it_products_instance = self.get_object()
        for key, value in combined_data.items():
            setattr(it_products_instance, key, value)
        it_products_instance.save()

        return redirect('itassets:It_Asset_Display')
    
def ItAssetDetailView(request,id):
    if request.method == "POST":
        print("post")
    else:
        try:
            # Assuming 'It_Products' is the name of your model  
            itassetdetail_obj = It_Prodcuts.objects.get(id=id)
          
            # Do something with the retrieved object
            
            if itassetdetail_obj.current_allocation :
                allocation_id = itassetdetail_obj.current_allocation.id
                allocation_details = ItAssetAllocation.objects.select_related('serial_number', 'user').get(id=allocation_id)  
                context = {
                        'itassetdetail_obj': itassetdetail_obj,
                        'allocationdetails': allocation_details,
                    }
            else:
                context = {
                        'itassetdetail_obj': itassetdetail_obj,
                        
                    }
                
            
            return render(request, 'itassets/itassetdetailview.html', context)
        except It_Prodcuts.DoesNotExist:
            # Handle the case when the object with the specified ID does not exist
            return HttpResponse(f"The IT asset with id={id} does not exist.")
        
        except It_Prodcuts.MultipleObjectsReturned:
            # Handle the case when multiple objects with the same ID are returned
            return HttpResponse(f"Multiple IT assets with id={id} exist.")
        """ except Exception as e:
         error_message = f"An error occurred: {str(e)}"
         return render(request, 'travelclaim/error_template.html', {'error_message': error_message}) """
    
def itassetdisplay(request):
    if request.method=="POST":
        print("post")
    else:
        ItProducts_obj = It_Prodcuts.objects.all()
       
        
        context = {
            'form' : ItProducts_obj,
           
            
           }
        
        return render(request,'itassets/itproductfilter.html',context)
    
def itassetfilter(request):
    try:
            if request.method=="GET":
                status = request.GET.getlist('status[]')
                allocation_status = request.GET.getlist('allocation_status[]')
                station_name = request.GET.getlist('station_name[]')
                category = request.GET.getlist('category[]')
                all_products = It_Prodcuts.objects.all().order_by('-id')
            
                if len(status) >0:
                    all_products = all_products.filter(status__id__in=status)
                    
                if len(allocation_status) >0:
                    all_products = all_products.filter(allocation_status__id__in=allocation_status)
                if len(station_name) >0:
                    all_products = all_products.filter(station_name__id__in=station_name)
                if len(category) >0:
                    all_products = all_products.filter(category__id__in=category)
                if not all_products.exists():
                # No products available after filtering
                    return JsonResponse({'success': True, 'filter_results_html': '<p>No products available</p>'})
                
                context={
                    'result': all_products
                }
                if "4" in category:
                    template_name = 'itassets/itproductfilterajax_cctv.html'
                    print("ajmal")
                elif '3' in category:
                    template_name = 'itassets/itproductfilterajax_Printer.html'
                elif '8' in category:
                    template_name = 'itassets/itproductfilterajax_ipphone.html'
                else:
                    template_name = 'itassets/itproductfilterajax.html'
                
                template = get_template(template_name)
                form_html = template.render(context)
               
                #form_html = render(request, 'itassets/itproductfilterajax.html', context).content.decode('utf-8')
                return JsonResponse({'success': True, 'filter_results_html': form_html})
                
    except Exception as e:
        return JsonResponse({'success': False, 'error_message': str(e)})
    

def test_deallocate_asset(request,id):
    
    try:
        if request.method == 'POST':
            print("post")
        else:
            deallocate_asset = It_Prodcuts.objects.get(id=id)
            stock_allocation_status = Allocation_status.objects.get(pk=2)
            
            if deallocate_asset:
                deallocate_asset.allocation_status = stock_allocation_status
                deallocate_asset.save()
                
            

            allocation_id = deallocate_asset.current_allocation.id
            
            
            table_allocation = ItAssetAllocation.objects.get(id=allocation_id, serial_number=id, deallocation_date__isnull=True)

            if table_allocation :
                table_allocation.deallocation_date = timezone.now()
                table_allocation.save()
                return HttpResponse("product checkedout succesfully")

    except Exception as e:
        # Handle exceptions here, log the error, and return an appropriate response
        return HttpResponse(f'Error during deallocation: {str(e)}', status=500)
    
        
        

def deallocate_asset(asset):
    
    current_allocation = ItAssetAllocation.objects.filter(serial_number=asset, deallocation_date__isnull=True).first()
    product_allocation_status=It_Prodcuts.objects.get(pk=asset)
    stock_allocation_status = Allocation_status.objects.get(pk=2)
    
    
    if current_allocation:
        # Mark deallocation date
        current_allocation.deallocation_date = timezone.now()
        current_allocation.save()
        product_allocation_status.allocation_status = stock_allocation_status
        product_allocation_status.save()
       
        return True
    else:
        return False

#test
def allocate_asset_test(request,id):
    if request.method == "POST":
        print("post")
        
    else:
        asset_id = id
        form = ItAssetHandOverForm(asset_id)
        Asset_details = It_Prodcuts.objects.get(id=asset_id)
        
        context = {
            'form': form,
            'itassetdetail_obj' :Asset_details
            
        }
        return render(request, 'itassets/allocate_it_asset.html', context)
    
def allocate_asset_view(request,id):
    if request.method == "POST":
        print("post")
        
    else:
        asset_id = id
        form = ItAssetAllocationForm(asset_id)
        Asset_details = It_Prodcuts.objects.get(id=asset_id)
        
        context = {
            'form': form,
            'itassetdetail_obj' :Asset_details
            
        }
        return render(request, 'itassets/allocate_it_asset.html', context)
    


def allocate_it_asset(request):
    try:
        if request.method == 'POST':
            
            asset_serial_id = request.POST.get('hidden_field')
            user_id = request.POST.get('user')

            allocation_date = timezone.now()
            
            # Retrieve instances or return a 404 response if not found
            s_instance = get_object_or_404(It_Prodcuts, pk=asset_serial_id)
            u_instance = get_object_or_404(CustomUser, pk=user_id)

            # Create a new ItAssetAllocation instance
            instance = ItAssetAllocation.objects.create(
                serial_number=s_instance,
                allocation_date=allocation_date,
                user=u_instance
            )

            # Update allocation status and current allocation for the ItProduct
            in_use_status = get_object_or_404(Allocation_status, pk=1)
            s_instance.allocation_status = in_use_status
            s_instance.current_allocation = instance
            s_instance.save()

            return HttpResponse('allocation_success')
    except Exception as e:
        # Handle exceptions here, log the error, and return an appropriate response
        return HttpResponse(f'Error during allocation: {str(e)}', status=500)
        
#test
def assetllocationtest(request):
    try:
        if request.method == "POST":
            
            testid = request.POST.get("hidden_field")
            asset_details = It_Prodcuts.objects.get(id=testid)
            
          
            form = ItAssetAllocationForm(testid,request.POST)
          

            if form.is_valid():
                instance =form.save(commit=False)
                
                instance.serial_number = asset_details
                instance.save()
                 # Update allocation status and current allocation for the ItProduct
                in_use_status = get_object_or_404(Allocation_status, pk=1)
                asset_details.allocation_status = in_use_status
                asset_details.current_allocation = instance
                asset_details.save()
                return HttpResponse('Form submitted')
            else:
                print(form.errors)
                form = ItAssetAllocationForm(testid,request.POST)
                context = {
                            'form': form,
                             }
                return render(request, 'itassets/allocate_it_asset.html', context)
        else:
            return HttpResponse('Invalid request method')
    except Exception as e:
        return HttpResponse(f'An error occurred: {str(e)}')
        
      
        

def get_serial_asset(request):
    if request.method == "POST":
        print("post")
        
    else:
        serialnumber = request.GET.get('serialnumber')
        Asset = It_Prodcuts.objects.get(pk=serialnumber)
        context={
                    'itassetdetail_obj': Asset
                }
                
        
        form_html = render(request, 'itassets/itproductdetailsajax.html', context).content.decode('utf-8')
        return JsonResponse({'success': True, 'filter_results_html': form_html})
            
def get_user_details(request):
    try:
        if request.method == "POST":
            print("post")
        else:
            userid = request.GET.get('userid')
            
            
            user = CustomUser.objects.get(pk=userid)
            context = {
                'itassetdetail_obj': user
            }

            form_html = render(request, 'itassets/itproductuserajax.html', context).content.decode('utf-8')
            return JsonResponse({'success': True, 'filter_results_html': form_html})
    except ObjectDoesNotExist as e:
        return JsonResponse({'success': False, 'error_message': str(e)})
    except Exception as e:
        return JsonResponse({'success': False, 'error_message': str(e)})
    
    
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)

    result = BytesIO()
 
    
    # Set the pagesize to A4
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, pagesize="A4")
    
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
    

def htmltopdf(request,id):
    itassetdetail_obj = It_Prodcuts.objects.get(id=id)
            # Do something with the retrieved object
    allocation_id = itassetdetail_obj.current_allocation.id
    allocation_details = ItAssetAllocation.objects.select_related('serial_number','user').get(id=allocation_id)
    context ={
                'itassetdetail_obj': itassetdetail_obj,
                'allocationdetails' : allocation_details,
                'current_time' : timezone.now(),
                 
                 
            }
    
    pdf = render_to_pdf('itassets/itassetdetailview copy.html', context)
   
    
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="Sats Asset Allocation.pdf"'
        return response

    return HttpResponse("Error generating the PDF", status=500)

def ItModal_Ajaxautocomplete(request):
    term = request.GET.get('term', '')
    print(term)  # Get the search term from the request
    suggestions = It_Prodcuts.objects.filter(model__icontains=term).values_list('model', flat=True) 
    return JsonResponse(list(suggestions), safe=False)

def Ajax_display_ItBrand(request):
    if request.method== 'POST':
     print("post")
    else:

        itbrandform = ITBrandsForm()
        form_html = render(request, 'itassets/ajax_error_Addbrand.html', {'form': itbrandform}).content.decode('utf-8')
        return JsonResponse({'success': True, 'data': form_html}) 



def Save_ItBrand(request):
    if request.method == 'POST':
        form = ITBrandsForm(request.POST)
        if form.is_valid():
            new_brand= form.save()
            return JsonResponse({'success': True,'id': new_brand.id, 'name': new_brand.brand, 'data':'form submitted'})
        else:
            form_html = render(request, 'itassets/ajax_error_Addbrand.html', {'form': form}).content.decode('utf-8')
            return JsonResponse({'success': False, 'data': form_html}) 
        

def Ajax_display_ItCategory(request):
    if request.method== 'POST':
     print("post")
    else:

        itcategoryform= ITCategoryForm()
        form_html = render(request, 'itassets/ajax_error_Addcategory.html', {'form': itcategoryform}).content.decode('utf-8')
        return JsonResponse({'success': True, 'data': form_html}) 

        
def Save_ItCategory(request):
    if request.method == 'POST':
        form = ITCategoryForm(request.POST)
        if form.is_valid():
            new_category= form.save()
            return JsonResponse({'success': True,'id': new_category.id, 'name': new_category.category, 'data':'form submitted'})
        else:
            form_html = render(request, 'itassets/ajax_error_Addcategory.html', {'form': form}).content.decode('utf-8')
            return JsonResponse({'success': False, 'data': form_html}) 


def get_brand_and_category(request):
    model_id = request.GET.get('model_id')
    if model_id:
        
        model = It_Model.objects.get(id=model_id)
        
        data = {
            'brand_id': model.brand.id,
            'brand_name': model.brand.brand,
            'category_id': model.category.id,
            'category_name': model.category.category
        }
       
        return JsonResponse(data)
    return JsonResponse({'error': 'Model ID not provided'})

def Ajax_display_ItModel(request):
    if request.method== 'POST':
     print("post")
    else:

        itmodelform = ITModelForm()
        form_html = render(request, 'itassets/ajax_Itmodalform.html', {'form': itmodelform}).content.decode('utf-8')
        return JsonResponse({'success': True, 'data': form_html}) 
    
def Ajax_Save_ItModel(request):
    if request.method == 'POST':
        itmodelform = ITModelForm(request.POST)
        if itmodelform.is_valid():
            new_model= itmodelform.save()
            return JsonResponse({'success': True,'id': new_model.id,'model_name': new_model.model_name, 'data':'form submitted'})
        else:
            form_html = render(request, 'itassets/ajax_Itmodalform.html', {'form': itmodelform}).content.decode('utf-8')
            return JsonResponse({'success': False, 'data': form_html}) 
        

def create_maintenance_request(request):

    
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,'Maintanence request issued succesfully')
            return redirect ('itassets:itassetdisplay')
        
        else:
             context={
            'form': form,
            
            }
             
             return render(request, 'itassets/maintenance_request_form.html',context)
    else:
        form = MaintenanceRequestForm()
        context={
            'form': form,
          

            }
    
        return render(request, 'itassets/maintenance_request_form.html',context)
    
@login_required 
def create_maintenance_requestid(request,id=None):
    if id is not None:
      
        it_product = get_object_or_404(It_Prodcuts, id=id)
    else:
        it_product = None
    
    if request.method == 'POST':
        
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            maintenance_request = form.save(commit=False)
            if it_product:
                status = It_Device_Status.objects.get(status='Inactive')
                # Update the status of the It_Prodcuts instance
                it_product.status = status
                it_product.save()
                maintenance_request.it_product = it_product 
                maintenance_request.Created_By = request.user
                maintenance_request.save()
                messages.success(request,'Maintanence request issued succesfully')
                return redirect ('itassets:itassetdisplay')
        
        else:
             context={
            'form': form,
            
            }
             
             return render(request, 'itassets/maintenance_request_form.html',context)
        
    else:
        initial_data = {'it_product': it_product} if it_product else {}
        form = MaintenanceRequestForm(initial=initial_data)
        context = {
            'form': form,
            'it_product': it_product
        }
        return render(request, 'itassets/maintenance_request_form.html', context)
    

    
@login_required 
def Edit_maintenance_requestid(request,id=None):
    maintenance_request = get_object_or_404(MaintenanceRequest, id=id)
    if request.method == "POST":
        
        form = MaintenanceEditForm(request.POST,request.FILES, instance=maintenance_request)
        if form.is_valid():
            it_product_hidden = form.cleaned_data['it_product_hidden']
            
            # Now you can use the value of it_product_hidden instead of it_product
            # For example, you might want to save it to the database
            # Assuming YourModelName is the model associated with the form
            instance = form.save(commit=False)
            instance.it_product = it_product_hidden
            instance.Created_By = request.user
            instance.save()
            messages.success(request,'Maintanence request updated succesfully')
            return redirect ('itassets:itassetdisplay')
        else:
       
            return render(request, 'itassets/edit_maintenance_request.html', {'form': form})

    else:
        form = MaintenanceEditForm(instance=maintenance_request)
    return render(request, 'itassets/edit_maintenance_request.html', {'form': form})

def Maint_update_history_view(request):
    history_entries = Maint_Request_history.objects.all()
    for entry in history_entries:
        if entry.changes:
            entry.parsed_changes = ast.literal_eval(entry.changes)
    return render(request, 'itassets/it_maint_update_history.html', {'history_entries': history_entries})



def serial_bulkupdate(request):

    if request.method == 'POST':
    # Iterate over the POST data to get the updated serial numbers
        for key, value in request.POST.items():
            if key.startswith('serial_number_'):
                serial_number = key.replace('serial_number_', '')
                new_serial_number = value
    # Update the serial number in the database
                It_Prodcuts.objects.filter(serial_number=serial_number).update(serial_number=new_serial_number)
    # Redirect to a success page or return a success message
        return redirect ('itassets:itassetdisplay')
    else:

        cctv_serial_numbers = It_Prodcuts.objects.filter(category=4)

        context = {
            'cctv_serial_numbers': cctv_serial_numbers,
        }
    return render(request, 'itassets/it_bulkupdate.html', context)