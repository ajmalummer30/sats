from email import message
from lib2to3.pgen2 import driver
from multiprocessing import context
from urllib import request
from django import http
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import requests
from twilio.rest import Client
from accounts.models import CustomUser
from myproject.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from django.shortcuts import get_object_or_404
from pettycash.models import TravelClaim
from quality.forms import DriverForm, IncidentReportingForm
from quality.models import Country, DriverInvolved, Employeesinvolved, In_Incidents, States
from rest_framework import generics  
from .serializers import  CountrySerializer, DriverInvolvedSerializer, EmployeesinvolvedDetailSerializer, EmployeesinvolvedSerializer, StateSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from requests.auth import HTTPBasicAuth
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly




# Create your views here.

def home(request):
    if request.method == 'POST':
        print('post')
        
    else:
        
        return render(request,'quality/htmx.html')
    
def mouse_entered(request):
    if request.method == 'POST':
        return HttpResponse('POST request received') 
        
    else:
        
        return HttpResponse('this is a mouse enter function')
    

def username(request):
    if request.method == 'POST':
        username = request.POST.get('q') 
        
        if CustomUser.objects.filter(username=username).exists():
            return HttpResponse('<div class="exist" style="color: red;">Username exists</div>')  # Username already taken
        else:
            return HttpResponse('<div class="available" style="color: green;">Username available</div>')  # Username is available
    return HttpResponse('Invalid request method', status=405)

""" def home(request):
    if request.method == 'POST':
        form=IncidentReportingForm(request.POST,request.FILES)
     
        if form.is_valid():
           instance= form.save()
           messages.success(request,'Form saved succesfully')
           return redirect('quality:listincidents')
        else:
            #return HttpResponse(form.errors)
            return render(request,'quality\incident_report.html',{'form':form})
    else:
        form = IncidentReportingForm()
        driverform =DriverForm()
        context={
            'form': form,
            'driverform':driverform
            
            
        }
        
        return render(request,'quality/incident_report.html',context)
         """
def SaveDriverinfo(request):
    if request.method == 'POST':
        driverform = DriverForm(request.POST)
        if driverform.is_valid():
            new_driver= driverform.save()
            return JsonResponse({'success': True,'id': new_driver.id, 'name': new_driver.name, 'data':'form submitted'})
        else:
            errors = {}
            for field, field_errors in driverform.errors.items():
                errors[field] = [error for error in field_errors]
            return JsonResponse({'success': False, 'errors': driverform.errors})
        # Redirect to a URL or view name
    else:
        driverform = DriverForm()

    return render(request, 'quality/incident_report.html', {'driverform': driverform})
            
            
def listincidents(request):
    if request.method =='POST':
        print("post")
    else :
        incident_obj = In_Incidents.objects.all().order_by('-created_date')
        return render(request,'quality/list_incidents.html',{'incident_obj':incident_obj} )

def incidentdetailview(request,id):
    if request.method =='POST':
        print("post")
    else :
        incident_obj = In_Incidents.objects.get(id=id)
        return render(request,'quality/incident_detailview.html',{'incident_obj':incident_obj} )
            
        
            
    
        
        
def send_notification(request):
    order_details = {
    'amount': '5kg',
    'item': 'Tomatoes',
    'date_of_delivery': '03/04/2021',
    'address': 'No 1, Ciroma Chukwuma Adekunle Street, Ikeja, Lagos'
        }
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    document = TravelClaim.objects.get(id=9)
    print(document)
    pdf_url = request.build_absolute_uri(document.upload_bill.url)
    phone = CustomUser.objects.all()
    
    if request.method == 'POST':
        
        
        #user_whatsapp_number = request.POST.get('user_number')
            phone_number =966580656544
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body='Your {} order of {} has shipped and should be delivered on {}. Details: {}'.format(
                    order_details['amount'], order_details['item'], order_details['date_of_delivery'],
                    order_details['address']),
                to='whatsapp:+{}'.format(phone_number),
                 #media_url=[pdf_url]
            )
            
      
            print(pdf_url)
            print(message.sid)
            return HttpResponse('Great! Expect a message...')

    return render(request, 'quality/phone.html')

        
class EmployeeCreateView(generics.ListCreateAPIView):
    queryset = Employeesinvolved.objects.all()
    serializer_class = EmployeesinvolvedSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employeesinvolved.objects.all()
    serializer_class = EmployeesinvolvedSerializer 
    
    
class DriverViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DriverInvolved.objects.all()
    serializer_class = DriverInvolvedSerializer
    permission_classes = [IsAuthenticated]
    
class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    

class StatesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = States.objects.all()
    serializer_class = StateSerializer
    permission_classes = [AllowAny]
    
    def list(self, request, *args, **kwargs):
        country_id = request.query_params.get('country_id', None)
        if country_id is not None:
            queryset = States.objects.filter(country__id=country_id)
        else:
            queryset = self.queryset

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing book instances.
    """
    queryset = Employeesinvolved.objects.all()
    serializer_class = EmployeesinvolvedSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    
    def list(self, request, *args, **kwargs):
        # Custom GET logic here
        employees = Employeesinvolved.objects.all()  
        serializer = EmployeesinvolvedDetailSerializer(employees, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        # Override the retrieve logic to use EmployeesinvolvedDetailSerializer
        employee = self.get_object()
        serializer = EmployeesinvolvedDetailSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # Override POST (create) logic
    def create(self, request, *args, **kwargs):
        # Custom POST logic here
        
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            
            # Example: Custom logic before saving
            print("Creating a new employee")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def update(self, request, pk=None):
        
        
        employee = self.get_object()
        serializer = self.get_serializer(employee, data=request.data, partial=False)
        if serializer.is_valid():
            
            # Example: Custom logic before saving
            print("Creating a new employee")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
       

# application teste uisng django's DRF token auth & authorisation & get method
def test_get_and_post_api(request):
    try:
        # Simulating a GET request to your own API
        get_url = f'http://127.0.0.1:8000/safety/api-token-auth/'
        
        username = 'ajmalummer'
        password = 'Welcome2s'    
        
        data={
            'username' : username,
            'password' : password   
        }
    
    
        
        # Make a GET request with Basic Authentication
        response = requests.post(get_url,data=data)
        if response.status_code == 200:
        # Print the GET response (list of employees)
            print("GET Response:", response.json())
            token_data = response.json()
            
            token = token_data.get('token')
            
            # Now that you have the token, make a GET request to the protected endpoint
            get_employee_url = f'http://127.0.0.1:8000/safety/employee/'
            headers = {
                'Authorization': f'Token {token}'
            }
            
             # Make a GET request to the employees API endpoint with the token
            employee_response = requests.get(get_employee_url, headers=headers)
            
            if response.status_code == 200:
                employee_data = employee_response.json()
                print("GET Response - Employees:", employee_data)

            # Return the data as a JsonResponse. Set safe=False if it's a list.
                return JsonResponse(employee_data, safe=False)
            else:
                # Handle error in employee GET request
                return JsonResponse({"error": "Failed to retrieve employee data", "status_code": employee_response.status_code}, status=employee_response.status_code)
        
        else:
            # Handle error in token POST request
            return JsonResponse({"error": "Failed to authenticate", "status_code": response.status_code}, status=response.status_code)
    
            
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)




def test_get_and_post_api_jwt(request):
    try:
        # Simulating a GET request to your own API
        get_url = f'http://127.0.0.1:8000/safety/api/token/'
        
        
        username = 'ajmalummer'
        password = 'Welcome2s'    
        
        data={
            'username' : username,
            'password' : password   
        }
    
    
        
        # Make a GET request with Basic Authentication
        response = requests.post(get_url,data=data)
        if response.status_code == 200:
        # Print the GET response (list of employees)
            print("GET Response:", response.json())
            token_data = response.json()
            
            access_token = token_data.get('access')
            refresh_token = token_data.get('refresh')
            
            return make_api_request(access_token, refresh_token)
        
        return JsonResponse({"error": "Authentication failed"}, status=401)
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)
    
def make_api_request(access_token, refresh_token):
    try: 
            
            # Now that you have the token, make a GET request to the protected endpoint
            get_employee_url = f'http://127.0.0.1:8000/safety/employee/'
            headers = {
                'Authorization': f'Bearer {access_token}'  # Correct format: Bearer <access_token>
            }
            
             # Make a GET request to the employees API endpoint with the token
            employee_response = requests.get(get_employee_url, headers=headers)
            
            if employee_response.status_code == 200:
                employee_data = employee_response.json()
                print("GET Response - Employees:", employee_data)

            # Return the data as a JsonResponse. Set safe=False if it's a list.
                return JsonResponse(employee_data, safe=False)
            elif employee_response.status_code == 401:
            # Access token has expired, let's refresh it
                  return refresh_access_token(refresh_token)
            else:
                # Handle error in employee GET request
                return JsonResponse({"error": "Failed to retrieve employee data", "status_code": employee_response.status_code}, status=employee_response.status_code)
            
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)


def refresh_access_token(refresh_token):
    try:
        # URL to refresh the access token
        refresh_url = 'http://127.0.0.1:8000/safety/api/token/refresh/'
        
        # Request payload to refresh the token
        data = {'refresh': refresh_token}
        
        # POST request to get a new access token
        response = requests.post(refresh_url, data=data)
        
        if response.status_code == 200:
            # New access token received
            new_access_token = response.json().get('access')
            # Retry the API request with the new access token
            return make_api_request(new_access_token, refresh_token)
        
        return JsonResponse({"error": "Refresh token expired, please log in again"}, status=401)
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)