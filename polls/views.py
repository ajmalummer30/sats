
import io
import json
import os
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from reportlab.lib.colors import HexColor
from datetime import datetime, timedelta
from django.utils import timezone
from requests import Response
#from accounts import forms
from accounts.models import Station
from myproject.tasks import add
from polls.forms import  CM_WorkPermitForm, CMCommentForm, ContractorForm, Fa_CMFileuploadForm, Fa_CMForm, Fa_CategoryForm, Fa_ContractForm, Fa_FileuploadForm, Fa_NewFileuploadForm, Fa_NewWorkForm, Fa_PMFileuploadForm, Fa_PMForm, Fa_SubCategoryForm, GatePassForm, GatepassItemForm, GenQuestionForm, IncidentForm, New_WorkPermitForm, NewCommentForm, PM_WorkPermitForm, PMCommentForm, SubQuestionForm, SubjectDropdownForm, SubjectQuestionFrom, WorkPermitFilterForm, WorkPermitForm, WorkerForm
from .models import ChecklistDetails, Contractor, CorrectiveMaintenance, Equipment, EquipmentSpecificQuestion, ExcelFile, Fa_Category, Fa_Contract, Fa_SubCategory, Fuel, GatePassModel, Gatepass_Items_Model, GenQuestionResponse, NewMaintanence, PreventiveMaintenance, SubQuestionResponse, GeneralQuestion, Workorder, Workpermit
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from io import BytesIO
from urllib import request, response
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle,Image
import qrcode
#from PIL import Image as PILImage
#from PIL import ImageEnhance
from reportlab.lib import colors
from django.contrib.staticfiles import finders
from reportlab.lib.styles import getSampleStyleSheet
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import pandas as pd
from django.conf import settings
from .resources import PersonResource
from tablib import Dataset
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.views.decorators.http import require_POST
from django.db.models import Q







def home(request):
    try:
        #subjects = Equipment.objects.all()
        drpform = SubjectDropdownForm(request.user)
        

        context = {
            'drpform': drpform
            
        }
        #send_mail(subject, message, sender_email, recipient_list)
        return render(request,'polls/index.html', context)

    except Exception as e:
        # Handle the exception
        if str(e) == "'AnonymousUser' object has no attribute 'station_name'":
            error = "Please login first"
        
        
        error_message = f"An error occurred: {str(e)}. Please login first."
        
        # Log the error or send an email notification
        """ send_mail(
            'Error on your website',
            error_message,
            'your@example.com',  # Replace with your email address
            ['admin@example.com'],  # Replace with the recipient's email address
            fail_silently=False,
        ) """

        # Add a message for the user (optional)
        messages.error(request, error)

        # Render a custom error page or redirect to another page
        return render(request, 'polls/index.html', {})

def facility_menu(request):

    res=add.delay(4,8)
    try:
        res_value = res.get(timeout=10)
        print(f"Result : {res_value}")
    except Exception as e:
        res_value = None
        print(f"An error occurred: {e}")
          
    return render(request,'facilityhomepage.html')


def generate_pdf(id):
    
    Genquestions_response = GenQuestionResponse.objects.filter(checklistid=id)
    Subquestions_response = SubQuestionResponse.objects.filter(checklistid=id)
    checklist = ChecklistDetails.objects.select_related('equipment','user').filter(id=id)
    
    
    for items in checklist:
        equipment_name = items.equipment
        
    
    for item in Genquestions_response:
        if item.response == '1':
            item.response = 'YES'
        else:
            item.response = 'NO'
    for item in Subquestions_response:
        if item.response == '1':
            item.response = 'YES'
        else:
            item.response = 'NO'
            
    #set A4 properties
    buffer = BytesIO()

    c = canvas.Canvas(buffer,pagesize=A4)
    grey_value = 0.5 
    # Draw Main Heading border
    c.setStrokeColorRGB(0.5, 0.5, 0.5)
    c.rect(32, A4[1]-90, width=142, height=60)
    c.rect(176, A4[1]-90, width=242, height=60)
    c.rect(420, A4[1]-90, width=144, height=60)# Draw a rectangle (x, y, width, height)

    
    # Set font and size for Main heading
    c.setFont("Helvetica-Bold", 14)
    c.setStrokeColorRGB(grey_value, grey_value, grey_value)
    c.drawString(230, A4[1] - 70, "Checklist Details")
    
    
    # Draw the title
    c.setFont("Helvetica", 8)
    
    hex_color = colors.HexColor("#E5E4E2") 
    c.setFillColorRGB(grey_value, grey_value, grey_value)
    c.drawString(40, A4[1] - 60, "SATS/KSA/FM/K/001")

    # Set font for invoice details & ITEMS
    c.setFont("Helvetica", 12)
    
      #Add SATS LOGO
        
    image_path = finders.find('sats Saudi arabia.jpg')
    watermark_path = finders.find('satsgroupcmyk.png')
    
    if image_path:
        c.drawImage(image_path, x=443, y=A4[1] - 85, width=90, height=50)
    
    # Add other fields as needed
    
    Common_starting_height = A4[1] - 280 
    
    margin = 30  # 1 inch margin (72 points per inch)
    border_width = 2  # Set the border width
    gap=2
    line_width = 0.5
    # Calculate the coordinates for the border
    """ border_x1 = margin
    border_y1 = margin
    border_x2 = A4[0] - margin
    border_y2 = A4[1] - margin """
    # Draw a singleline  border around the entire page
    #c.rect(border_x1, border_y1, border_x2 - border_x1, border_y2 - border_y1, stroke=1)
      # Set border color (black)
    # Draw a multiline  border around the entire page
    for i in range(border_width):
        c.setLineWidth(line_width)
        c.rect(margin - i * gap, margin - i * gap, A4[0] - 2 * (margin - i * gap), A4[1] - 2 * (margin - i * gap), stroke=1)

    



    #details_string = '\n'.join([f"{key}: {value}" for obj in checklist for key, value in obj.__dict__.items()])
    for value in checklist:
        details_string = f"CHECKLIST REF NO: {value.id}\nEQUIPMENT NAME: {value.equipment}\nDRIVER: {value.user}\nCreated Date: {value.date}\nTime: {value.time}"
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1,
            border=4,
        )
        #qr.add_data(f"{Title}, {Year}, {Description}")
    qr.add_data(details_string)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="brown", back_color="white")
    pil_image = qr_img.get_image()
   
                #  Save QR code image as BytesIO and convert to ReportLab Image
    qr_buffer = BytesIO()
    qr_img.save(qr_buffer,format='PNG')
    qr_buffer.seek(0)
    c.drawInlineImage(pil_image, 450, A4[1] - 200, width=60, height=60)

#Header Table

# Write Checklist details  
    common_detail_xaxis= 50 
    data = []
    
    for value in checklist:
        serial_number = value.equipment.Serial_Number
        capacity = value.equipment.Capacity
        brand = value.equipment.Brand
        Station = value.equipment.station_name
        First_Name = value.user.first_name
        Last_Name = value.user.last_name
        row = [
        [f"CHECKLIST REF NO",value.id],
        [f"STATION",Station],
        [f"EQUIPMENT NAME", value.equipment],
        [f"Serial Number" ,serial_number],
        [f"Capacity", capacity],
        [f"Brand", brand],
        [f"DRIVER", f"{First_Name} {Last_Name}" ],
        [f"Created Date", value.date],
        [f"Time" ,value.time],
        
        
        ] 
    data.extend(row)   
       
        
    Common_table = Table(data)
    Common_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1),  hex_color), 
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),  # Add borders to all cells
        #('BACKGROUND', (0, 0), (0, 0), (0, 0, 0)),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Align content to center
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font bold
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical alignment to middle
    ]))  
    
    
    col_widths = [130, 200]
    Common_table._argW[0] = col_widths[0]
    Common_table._argW[1] = col_widths[1]
    
    Common_table.wrapOn(c, A4[0], A4[1])
    Common_table.drawOn(c, common_detail_xaxis, Common_starting_height)
    
    #checklist table

    data = [
        ['CHECK LIST ITEMS','RESPONSE']
        ]
    # Populate table data with invoice items fetched from the database 
    
    
    for item in Genquestions_response:
       
        question = item.question
        Response = item.response
        data.append([question,Response])
        
    for item in Subquestions_response:
       
        question = item.question
        Response = item.response
        data.append([question,Response]) 
    

    # Create a table and define table style
    table = Table(data)
    
    style= TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0),hex_color ),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Default gridlines for all cells
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.black),  # Header line weight (thicker)
        ('TOPPADDING', (0, 0), (-1, -1), 4),  # Adding padding to separate lines
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        
        
    ])
    #highlight rows with NO in RED COLOR
    style_red_text = getSampleStyleSheet()['BodyText']
    style_red_text.textColor = colors.red
    for row_index, row in enumerate(data):
        if 'NO' in row:  # Check if 'NO' exists in the row
            table.setStyle(TableStyle([ 
                ('TEXTCOLOR', (0, row_index), (-1, row_index), colors.red)  # Apply red text color to the entire row
            ]))
        else:
            table.setStyle(style)
            style.add('GRID', (0, 1), (-1, -1), 0.5, colors.black)
     #highlight colomn with NO in RED COLOR
    """ for row_index, row in enumerate(data):
        for col_index, cell_value in enumerate(row):
            if cell_value == 'NO':
                table.setStyle(TableStyle([
                    ('TEXTCOLOR', (col_index, row_index), (col_index, row_index), colors.red)
                ]))
            else:
                table.setStyle(style) """
    
    # Draw the table on the canvas
    table_starting_height = A4[1] -600
    table.wrapOn(c, A4[0], A4[1])
    table.drawOn(c, 50, table_starting_height)
    
    c.showPage()
    c.save()
    #buffer.seek(0)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    
    #Save the generated PDF

    shared_folder_path = '//192.168.1.110/facility dmm/Work permit/'
    
    today_date = datetime.now().strftime('%Y%m%d')
    
    shared_file_name = f'{today_date}_{equipment_name}_01.pdf'
    shared_file_path = os.path.join(shared_folder_path, shared_file_name)
    count = 1
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{shared_file_name}"'
    while os.path.exists(shared_file_path):
        # Append a suffix to the file name if it already exists
        count += 1
        shared_file_name = f'{today_date}_{equipment_name}_{count:02d}.pdf'
        shared_file_path = os.path.join(shared_folder_path, shared_file_name)
        response['Content-Disposition'] = f'attachment; filename="{shared_file_name}"'
     
    with open(shared_file_path, 'wb') as pdf_file:
        pdf_file.write(pdf_bytes) 

    #for downloading the PDF
    
    
    context={
        
        'response' :response,# to download the pdf
        #'filepath' :shared_file_path,
        'filename' :shared_file_name,
        'buffer': pdf_bytes # to show the content of pdf in iframe.iframe must be defined inside html template
    }
    
    return context



def get_questions(request):
    
    if request.method == 'POST':
        user = request.user
        Subjectid = request.POST.get('subject')
        subject=Equipment.objects.get(pk=Subjectid)
        form1 =SubjectDropdownForm(request.user,request.POST)
        SubQuestionform= SubQuestionForm(subject,request.POST)
        
        
        if SubQuestionform.is_valid():
            Checklist_Details=ChecklistDetails.objects.create(equipment=subject,user=user) 
            last_instance = ChecklistDetails.objects.latest('id')
            for key, value in request.POST.items():
                
                if key.startswith('answer2_'):
                    sub_question_id = int(key.split('_')[1])
                    sub_question = EquipmentSpecificQuestion.objects.get(pk=sub_question_id)
                    sub_answer= value
                    #print(f"Question: {sub_question.text}, Selected Choice: {sub_answer}")
                    SubQuestionResponse.objects.create(question=sub_question, response=sub_answer,checklistid=Checklist_Details )
                    
            returndata = generate_pdf(last_instance.id)
            email = EmailMessage(
                subject='PDF Attachment',
                body='Please find the attached PDF file.',
                from_email='ajmal.ummer@sats.com.sa',
                to=['ajmalummer30@gmail.com','lazim.mohammed@sats.com.sa']  
                )
        
        
            email.attach(returndata['filename'], returndata['buffer'], 'application/pdf')
            
            data="PDF generated and saved to folder:"+returndata['filename']
            #To download PDF while saving use below
            #email.send()
            print("Email sent successfully!")
            #return returndata['response'] 
            # messages.success(request, data)
            return JsonResponse({'success': True, 'data': data})
            # Redirect to a success page after processing the data """
             
            
        else:
            
            form_html = render(request, 'polls/subject_specific_questions.html', {'Subform': SubQuestionform}).content.decode('utf-8')
            return JsonResponse({'success': True, 'data': form_html})      
    else:
            subject_id = request.GET.get('subject_id')
            subject = Equipment.objects.get(pk=subject_id)
            SubQuestionform =SubQuestionForm(subject)
            form_html = render(request, 'polls/subject_specific_questions.html', {'Subform': SubQuestionform}).content.decode('utf-8')
            return JsonResponse({'success': True, 'subject_specific_questions_html': form_html})
            
     
def display_checklist(request):
        if request.method == 'GET':
            checklist = ChecklistDetails.objects.all().order_by('-date','-time')
            
        return render(request, 'polls/ChecklistView.html', {'checklist': checklist})
 
    
def detail_view(request,id):
    Genquestions_response = GenQuestionResponse.objects.filter(checklistid=id)
    Subquestions_response = SubQuestionResponse.objects.filter(checklistid=id)
    
    for item in Genquestions_response:
        if item.response == '1':
            item.response = 'YES'
        else:
            item.response = 'NO'
    for item in Subquestions_response:
        if item.response == '1':
            item.response = 'YES'
        else:
            item.response = 'NO'
        
    context = {
        'Genrep':Genquestions_response,
        'Subrep':Subquestions_response,
        
    }
    
    return render(request, 'polls/DetailView.html',context)

@login_required
def create_questions(request):
    
    if request.method == 'POST':
        form = SubjectQuestionFrom(request.POST)
        fuel_hidden = request.POST.get('Electric_question')
        
        
        if form.is_valid():
            form.save(commit=False)
            Fuel_instance = Fuel.objects.get(fueltype=fuel_hidden)
            form.instance.fueltype = Fuel_instance
            form.save()
            return redirect('polls:create_questions')
        else:
            return render(request, 'polls/createquestionElectric.html',{ 'questionform' : form })
            
    else:
        if request.method == 'GET':
            
            form = SubjectQuestionFrom()
            Questions_Electric= EquipmentSpecificQuestion.objects.filter(fueltype=1)
            context ={
                'questionform' : form,
                'questions' :Questions_Electric
            }
            return render(request,'polls/createquestionElectric.html',context)
        
def UpdateQuestions(request,id):
    Update_item = EquipmentSpecificQuestion.objects.get(id=id)
    form = SubjectQuestionFrom(instance=Update_item)
    if request.method == 'POST':
        form = SubjectQuestionFrom(request.POST, instance=Update_item)
        if form.is_valid():
            form.save()
            return redirect('polls:create_questions')
        else:
            return render(request, 'polls/createquestionElectric.html',{ 'questionform' : form })
    else:
        return render(request, 'polls/createquestionElectric.html',{ 'questionform' : form })
        
def DeleteQuestions(request,id):
    EquipmentSpecificQuestion.objects.get(id=id).delete()
    return redirect('polls:create_questions')
    
@login_required
def create_Dieselquestions(request):
    
    if request.method == 'POST':
        form = SubjectQuestionFrom(request.POST)
        fuel_hidden = request.POST.get('Diesel_question')
        
        if form.is_valid():
            form.save(commit=False)
            Fuel_instance = Fuel.objects.get(fueltype=fuel_hidden)
            form.instance.fueltype = Fuel_instance
            form.save()
            return redirect('polls:create_Dieselquestions')
        else:
            return render(request, 'polls/createquestionDiesel.html',{ 'questionform' : form })
            
    else:
        if request.method == 'GET':
            form = SubjectQuestionFrom()
            Questions_Diesel= EquipmentSpecificQuestion.objects.filter(fueltype=2)
            context ={
                'questionform' : form,
                'questions' :Questions_Diesel
            }
            return render(request,'polls/createquestionDiesel.html',context)
    

def generate_invoice(request,id):
   
   
    
    Genquestions_response = GenQuestionResponse.objects.filter(checklistid=id)
    Subquestions_response = SubQuestionResponse.objects.filter(checklistid=id)
    checklist = ChecklistDetails.objects.select_related('equipment','user').filter(id=id)
    
    for items in checklist:
        equipment_name = items.equipment
    
    for item in Genquestions_response:
        if item.response == '1':
            item.response = 'YES'
        else:
            item.response = 'NO'
    for item in Subquestions_response:
        if item.response == '1':
            item.response = 'YES'
        else:
            item.response = 'NO'
            
   
   
    shared_folder_path = '//192.168.1.110/facility dmm/Work permit/'
    today_date = datetime.now().strftime('%Y%m%d')
    
    shared_file_name = f'{today_date}_{equipment_name}_01.pdf'
    shared_file_path = os.path.join(shared_folder_path, shared_file_name)
    count = 1
    while os.path.exists(shared_file_path):
        # Append a suffix to the file name if it already exists
        count += 1
        shared_file_name = f'{today_date}_{equipment_name}_{count:02d}.pdf'
        shared_file_path = os.path.join(shared_folder_path, shared_file_name)
    
    # Create a canvas (PDF document) with a specific size (here, letter size)
    #c = canvas.Canvas(response, pagesize=A4)
    c = canvas.Canvas(shared_file_path, pagesize=A4)
    
    # Set font and size
    c.setFont("Helvetica-Bold", 14)

    # Draw the title
    c.drawString(230, A4[1] - 70, "Checklist Details")

    # Set font for invoice details
    c.setFont("Helvetica", 12)
    
      #Add SATS LOGO
        
    image_path = finders.find('sats Saudi arabia.jpg')
    watermark_path = finders.find('satsgroupcmyk.png')
    
    if image_path:
        c.drawImage(image_path, x=40, y=A4[1] - 85, width=90, height=50)
        
   
    #ADD WATERMARK
    """ img_width, img_height = 200, 100  # Adjust image size as needed
    a4_width, a4_height = A4
    x = (a4_width - img_width) / 2  # Center X-coordinate
    y = (a4_height - img_height) / 2
    c.drawInlineImage(watermark_path, x, y, width=img_width, height=img_height) """

    # Set starting point for invoice details
      # Starting from the top of A4 page
    Common_starting_height = A4[1] - 250 
    
    margin = 30  # 1 inch margin (72 points per inch)
    border_width = 2  # Set the border width
    gap=2
    line_width = 0.5
    # Calculate the coordinates for the border
    """ border_x1 = margin
    border_y1 = margin
    border_x2 = A4[0] - margin
    border_y2 = A4[1] - margin """
    # Draw a singleline  border around the entire page
    #c.rect(border_x1, border_y1, border_x2 - border_x1, border_y2 - border_y1, stroke=1)
    c.setStrokeColorRGB(0.5, 0.5, 0.5)  # Set border color (black)
    # Draw a multiline  border around the entire page
    for i in range(border_width):
        c.setLineWidth(line_width)
        c.rect(margin - i * gap, margin - i * gap, A4[0] - 2 * (margin - i * gap), A4[1] - 2 * (margin - i * gap), stroke=1)

    #details_string = '\n'.join([f"{key}: {value}" for obj in checklist for key, value in obj.__dict__.items()])
    for value in checklist:
        details_string = f"CHECKLIST REF NO: {value.id}\nEQUIPMENT NAME: {value.equipment}\nDRIVER: {value.user}\nCreated Date: {value.date}\nTime: {value.time}"
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1,
            border=4,
        )
        #qr.add_data(f"{Title}, {Year}, {Description}")
    qr.add_data(details_string)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="brown", back_color="white")
    pil_image = qr_img.get_image()
   
                #  Save QR code image as BytesIO and convert to ReportLab Image
    qr_buffer = BytesIO()
    qr_img.save(qr_buffer,format='PNG')
    qr_buffer.seek(0)
    c.drawInlineImage(pil_image, 450, A4[1] - 150, width=60, height=60)
    
    
    
    # Write Checklist details  
    common_detail_xaxis= 50 
    data = []
    
    for value in checklist:
        serial_number = value.equipment.Serial_Number
        capacity = value.equipment.Capacity
        brand = value.equipment.Brand
        row = [
        [f"CHECKLIST REF NO",value.id],
        [f"EQUIPMENT NAME", value.equipment],
        [f"Serial Number" ,serial_number],
        [f"Capacity", capacity],
        [f"Brand", brand],
        [f"DRIVER", value.user],
        [f"Created Date", value.date],
        [f"Time" ,value.time],
        
        
        ] 
    data.extend(row)   
       
    hex_color = colors.HexColor("#E5E4E2")
    Common_table = Table(data)
    Common_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), hex_color), 
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),  # Add borders to all cells
        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Align content to center
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font bold
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical alignment to middle
    ]))  
    
    
    col_widths = [130, 200]
    Common_table._argW[0] = col_widths[0]
    Common_table._argW[1] = col_widths[1]
    
    Common_table.wrapOn(c, A4[0], A4[1])
    Common_table.drawOn(c, common_detail_xaxis, Common_starting_height)
    
    data = [
        ['Question','Response']
        ]
    # Populate table data with invoice items fetched from the database 
    
    
    for item in Genquestions_response:
       
        question = item.question
        Response = item.response
        data.append([question,Response])
        
    for item in Subquestions_response:
       
        question = item.question
        Response = item.response
        data.append([question,Response]) 
    

    # Create a table and define table style
    table = Table(data)
    
    style= TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0),hex_color),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Default gridlines for all cells
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.black),  # Header line weight (thicker)
        ('TOPPADDING', (0, 0), (-1, -1), 4),  # Adding padding to separate lines
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        
        
    ])
    #highlight rows with NO in RED COLOR
    style_red_text = getSampleStyleSheet()['BodyText']
    style_red_text.textColor = colors.red
    for row_index, row in enumerate(data):
        if 'NO' in row:  # Check if 'NO' exists in the row
            table.setStyle(TableStyle([
                ('TEXTCOLOR', (0, row_index), (-1, row_index), colors.red)  # Apply red text color to the entire row
            ]))
        else:
            table.setStyle(style)
            style.add('GRID', (0, 1), (-1, -1), 0.5, colors.black)
     #highlight colomn with NO in RED COLOR
    """ for row_index, row in enumerate(data):
        for col_index, cell_value in enumerate(row):
            if cell_value == 'NO':
                table.setStyle(TableStyle([
                    ('TEXTCOLOR', (col_index, row_index), (col_index, row_index), colors.red)
                ]))
            else:
                table.setStyle(style) """
    
    # Draw the table on the canvas
    table_starting_height = A4[1] -600
    table.wrapOn(c, A4[0], A4[1])
    table.drawOn(c, 50, table_starting_height)

   # Create a ReportLab canvas
    

    c.save()
    qr_buffer.seek(0)
    response.write(qr_buffer.getvalue())
    qr_buffer.close()
 
# Call the function to generate the invoice
    #return response
    data="PDF generated and saved to folder:" + shared_file_path
    return HttpResponse(data)


def CreateWorkpermitView(request):
    
    if request.method =="POST":
        print('Ajmal')
        form=WorkPermitForm(request.POST, request.FILES)
      
        if form.is_valid():
           
            form.save()
             
            ref_obj = Workpermit.objects.latest('id')
            
            messages.success(request,' YOUR WORKPERMIT saved successfully. REF NO IS : ' + str(ref_obj.id)+ '. Please save the reference number for future reference')
            return redirect('polls:displayworkpermits')
        else:
           
            workerform = WorkerForm()
            contractorform =ContractorForm()
            context ={
            'form':form,
            'workerform': workerform,
            'contractorform' :contractorform

        }
            return render(request,'polls/createworkpermit.html',context)      
    else:
        form = WorkPermitForm()
        workerform =WorkerForm()
        contractorform =ContractorForm()
        
        context ={
            'form':form,
            'workerform': workerform,
            'contractorform' :contractorform

        }
        
        return render(request,'polls/createworkpermit.html',context)
    
def WorkpermitsDisplayView(request):
    
    if request.method == "POST":
        print("post")
        
    else:
        form= WorkPermitFilterForm()
        
        workpermit_obj = Workpermit.objects.all().order_by('-created_date')
        return render(request,'polls/WorkpermitView.html',{'obj' : workpermit_obj,'form':form})
    
    
def Editworkpermit(request,id):
    workpermit_obj = Workpermit.objects.get(id=id)
    if request.method=="POST":
        form = WorkPermitForm(request.POST,request.FILES,instance=workpermit_obj)
        if form.is_valid():
            form.save()
            messages.success(request,' YOUR WORKPERMIT updated successfully.')
            return redirect ('polls:displayworkpermits')
        else:
            return render(request, 'polls/createworkpermitcopy.html',{ 'form' : form })
    else:
        form = WorkPermitForm(instance=workpermit_obj)
        return render(request, 'polls/createworkpermitcopy.html',{ 'form' : form })
            
            
def DetailWorkpermitsView(request,id):
    
    
    if request.method == "POST":
        print("post")
        
    else:
        workpermit_obj = Workpermit.objects.filter(id=id)
        context ={
            'form' : workpermit_obj,
            'current_date' : timezone.now().date()
            
        }
        return render(request,'polls/WorkpermitDetailView.html',context)
    

def wppdfgenerate(request,id):
    
        hex_color = colors.HexColor("#E5E4E2")
        buffer = BytesIO()
         
        pdf = canvas.Canvas(buffer, pagesize=A4)
        elements = []
        grey_value = 0.5  
        pdf.setStrokeColorRGB(grey_value, grey_value, grey_value)
        pdf.rect(32, A4[1]-90, width=142, height=60)
        pdf.rect(176, A4[1]-90, width=242, height=60)
        pdf.rect(420, A4[1]-90, width=144, height=60)# Draw a rectangle (x, y, width, height)

    
    # Set font and size for Main heading
        pdf.setFont("Helvetica-Bold", 14)
    #c.setStrokeColorRGB(0.647, 0.165, 0.165)
        pdf.setStrokeColorRGB(0, 0, 0)
        pdf.drawString(230, A4[1] - 70, "WORK PERMIT")
      
    # Draw the title
        pdf.setFont("Helvetica", 8)
     
        pdf.setFillColorRGB(grey_value, grey_value, grey_value)
        pdf.drawString(40, A4[1] - 60, "SATS/KSA/FM/K/001")

        # Set font for invoice details & ITEMS
        pdf.setFont("Helvetica", 8)
    
      #Add SATS LOGO
        
        image_path = finders.find('satsksa.png')
    
        if image_path:
            pdf.drawImage(image_path, x=443, y=A4[1] - 85, width=90, height=50)
    
        # Add other fields as needed
    
        Common_starting_height = A4[1] - 200 
    
        margin = 30  # 1 inch margin (72 points per inch)
        border_width = 2  # Set the border width
        gap=2
        line_width = 0.5
            
            # Draw a multiline  border around the entire page
    
        for i in range(border_width):
            pdf.setLineWidth(line_width)
            pdf.rect(margin - i * gap, margin - i * gap, A4[0] - 2 * (margin - i * gap), A4[1] - 2 * (margin - i * gap), stroke=1)
            pdf.rect(370, 630, 10, 10)
            pdf.rect(420, 630, 10, 10)
            pdf.rect(470, 630, 10, 10)
            pdf.rect(520, 630, 10, 10)
        workpermit_obj = Workpermit.objects.get(id=id)
        workers_queryset = workpermit_obj.workers.all()
        
        worker_names = "\n".join(worker.Employee_name for worker in workers_queryset)
        worker_iqama_number = "\n".join(worker.Iqama_Number for worker in workers_queryset)
       
        
        
           
        data =[
                ["Permit Number","Start Date","END Date","","Station"],
                [workpermit_obj.id,workpermit_obj.start_date,workpermit_obj.end_date,'',workpermit_obj.station_name],
                ["Vendor Name","Staff Count","PPE: Tick the below"],
                [workpermit_obj.Contracting_Company_Name,workpermit_obj.Employee_Count,"Hard Hat","Safety Vest","Safety Shoe","Hand Gloves"],
                ["Vendor Supervisor Name","Iqama Number","Emergency Contact"],
                [workpermit_obj.Staff_in_charge,workpermit_obj.Iqama_number,workpermit_obj.Phone_number],
                ["worker names","iqama number","contact details"],
                [worker_names,worker_iqama_number,""],
                ["Scope of Work"],
                [workpermit_obj.Description],
                ["Remarks/Notes"],
                [workpermit_obj.Additional_notes],
                ["List of Tools"],
                [workpermit_obj.Tools],
                ["Safety Precuations","Hazardous Identification"],
                
            ]
        
        row=["","","","","",""]
            
        for i in range(2):
            data.append(row)

        #row_14=["worker names","iqama number","contact details"]
        #row_15=[worker_names,worker_iqama_number,""]
        row_16=["Approved By Facility","Noted by Security","Acknowledged by Contractor"]
        row_17=["Name:","Name:","Name:"]
        row_18=["Date:","Date::","Date:"]
        row_19=["Sign:","Sign:","Sign:"]
        
        
        #data.insert(14,row_14)
        #data.insert(15,row_15)
        data.insert(16,row_16)
        data.insert(17,row_17)
        data.insert(18,row_18)
        data.insert(19,row_19)
        
        col_widths= [150,150,50, 50 ,50,50]  
      
        row_heights = [20 if i % 2 == 0 else 35 for i in range(len(data))] 
        row_heights[7] = 100
        #row_heights[15] = 35
        row_heights[16] = 20
        row_heights[17] = 40
        row_heights[18] = 30
        row_heights[19] = 50

        
       
        
        
        table = Table(data,colWidths=col_widths,rowHeights=row_heights)
        style = TableStyle([
           
            # Header row background color
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header row text color
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alignment
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),  # Header row font style
            ('WORDWRAP', (0, 0), (-1, -1)), 
             ('WORDWRAP', (0, 3), (0, 3)), 
            ('ALIGN', (2, 3), (-1, 3), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('FONTSIZE', (0, 3), (-1, 3), 8),  
            ('SPAN', (2, 15), (-1, 15)),
            ('SPAN', (2, 16), (-1, 16)),
            ('SPAN', (2, 17), (-1, 17)),
            ('SPAN', (2, 18), (-1, 18)),
            ('SPAN', (2, 19), (-1, 19)),
            ('SPAN', (0, 20), (-1, 20)),
           
            
            ## Header row bottom padding
            ('GRID', (0, 0), (-1, -1), 0.3, colors.black),  # Gridlines
                ])
        
        for i in range(18):
            if i<=1:
                 table.setStyle(TableStyle([
                ('SPAN', (2, i), (-3, i)),
                ('SPAN', (4, i), (-1, i)) 
                    ]))
            if i==2:
                table.setStyle(TableStyle([
                ('SPAN', (2, i), (-1, i)) 
                    ]))
            
            if  4 <= i <= 7 or 14 <= i <= 18:
                table.setStyle(TableStyle([
                ('SPAN', (2, i), (-1, i)) 
                    ]))
            elif i>=8 and i<=13:
                table.setStyle(TableStyle([
                ('SPAN', (0, i), (-1, i))  # Apply red text color to the entire row
                    ]))
            if i % 2 == 0:
                table.setStyle(TableStyle([
                ('BACKGROUND', (0, i), (-1, i), hex_color),  # Apply red text color to the entire row
                    ]))
                
                
            
            
            
        table.setStyle(style)
        elements.append(table)
        table.wrapOn(pdf, 0, 0)
        table.drawOn(pdf, 50, 70)
            
        
        pdf.save()
        pdf_data = buffer.getvalue()
        buffer.close()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        # Write PDF data to the response
        response.write(pdf_data)
        return response
    
def import_data_to_db(request):
    data_to_display = None
    if request.method == 'POST':
        file = request.FILES['files']
        obj = ExcelFile.objects.create(
            file = file
        )
 
        path = file.file
 
         
        df = pd.read_excel(path)
 
        data_to_display = df.to_html()
 
    return render(request, 'polls/excel.html', {'data_to_display': data_to_display})


def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        new_persons = request.FILES['myfile']
        df = pd.read_excel(new_persons)
        
    
        dataset = Dataset().load(df)
        
        # Call the import_data hook and pass the tablib dataset
        result = person_resource.import_data(dataset,\
             dry_run=True, raise_errors = True)

        if not result.has_errors():
            result = person_resource.import_data(dataset, dry_run=False)
            return HttpResponse('data imported succesfully')

        return HttpResponse('data imported not succesfully')
    return render(request,"polls/import.html")
    
       
def incident_form(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            print(request.POST)
            user = request.user
            # Create a new Incident object with the user
            incident = form.save(commit=False)
            incident.user = user
            incident.save()
            # Save the many-to-many relationships for nature_of_injury
            form.save_m2m()
            messages.success(request, "the form saved succesfully")
            return render(request, 'polls/success.html', {'incident': incident})
        else:
            messages.error(request, 'Form not saved successfully.errors')
    else:
        # If it's a GET request, create a blank form
        
        form = IncidentForm(initial={'user': request.user})  # Set the initial value for the user field to the current user

    return render(request, 'polls/incident_form.html', {'form': form})
             
        
def Gatepass(request):
    if request.method == 'POST':
        form=GatePassForm(request.POST,request.FILES)
        if form.is_valid():
            user = request.user
            instance=form.save(commit=False)
            instance.user=user
            instance.save()
            # messages.success(request, "the form saved succesfully")
            return redirect ('polls:display_gatepass')
            
        else:
            messages.error(request, 'Form has validation errors',extra_tags='warning')
            return render(request,'polls/gatepassform.html',{'form':form})
        
        
    else:
        form = GatePassForm()
        return render(request,'polls/gatepassform.html',{'form':form})
    


def GatePassAddItems(request,id):
    if request.method == 'POST':
        form = GatepassItemForm(request.POST)
        Gatepass_obj = GatePassModel.objects.get(id=id)
        if form.is_valid():
           instance= form.save(commit=False)
           instance.GatePass = Gatepass_obj
           instance.save()
           gatepass_items =Gatepass_Items_Model.objects.filter(GatePass=id)
           return render (request, 'polls/DetailViewGatepass copy.html', {'gatepass_items': gatepass_items, 'id': id})
        else:
            gatepass_items =Gatepass_Items_Model.objects.filter(GatePass=id)
            context={
            'form' :form,
            'id' :id,
            'gatepass_items': gatepass_items,

                }
            return render(request,'polls/DetailViewGatepass copy.html',context)

        
    else:
        form = GatepassItemForm()
        gatepass_items =Gatepass_Items_Model.objects.filter(GatePass=id)
        context={
            'form' :form,
            'id' :id,
            'gatepass_items': gatepass_items

        }
        return render(request,'polls/DetailViewGatepass copy.html',context)
    



def Display_GatePass(request):
    if request.method == "POST":
        print("post")
        
    else:
        Gatepass_obj = GatePassModel.objects.all().order_by('-id')
        return render(request,'polls/GatepassView.html',{'form' : Gatepass_obj})
    
    
def Detail_gatepassView(request,id):
    if request.method == 'POST':
        print('POST')
    else:
        Gatepass_obj = GatePassModel.objects.get(id=id)
        context ={
            'Gatepass_obj':Gatepass_obj
        }
    return render(request,'polls/DetailViewGatepass.html',context)

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    else:
        return uri
    return path

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)

    result = BytesIO()
 
    
    # Set the pagesize to A4
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result,link_callback=link_callback, pagesize="A4")
    
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
    

def Detail_gatepassViewPdf(request,id):
    if request.method == 'POST':
        print('POST')
    else:
        Gatepass_obj = GatePassModel.objects.get(id=id)
        image_path = finders.find('sats Saudi arabia.jpg')
        print(image_path)
        context ={
            'Gatepass_obj':Gatepass_obj,
            'image_path': image_path,
        }
    #return render(request,'polls/DetailViewGatepass.html',context)
    pdf = render_to_pdf('polls/DetailViewGatepasspdf.html', context)
 
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="Gatepass.pdf"'
        return response

    return HttpResponse("Error generating the PDF", status=500) 




    

def update_return_dateAjax(request):
    if request.method =='POST':
        gatepass_id = request.POST.get('gatepass_id')
        try:
            # Assuming you have a GatePassModel model and want to update its return date
            gatepass_obj = GatePassModel.objects.get(pk=gatepass_id)
            gatepass_obj.Return_date = timezone.now().date()
            gatepass_obj.save()

            
            return JsonResponse({'success': True,'Return_date': str(gatepass_obj.Return_date), 'Gatepassno': gatepass_id})
        except GatePassModel.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Gatepass not found'}, status=404)
    else:
        return JsonResponse({'success': False, 'error': 'Not an AJAX request'}, status=400)
    




def Ajax_ShowWorkerModal(request):
    if request.method == 'POST':
        print("post")
    else:
        form = WorkerForm()
        form_html = render(request, 'polls/ajax_addworkers.html', {'form': form}).content.decode('utf-8')
        return JsonResponse({'success': True, 'data': form_html}) 

        
def SaveWorkerinfo(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST, request.FILES)
        if form.is_valid():
            new_worker= form.save()
            name = new_worker.Employee_name + ' ' + new_worker.Iqama_Number
            return JsonResponse({'success': True,'id': new_worker.id, 'name':name, 'data':'form submitted'})
        else:
            form_html = render(request, 'polls/ajax_addworkers.html', {'form': form}).content.decode('utf-8')
            return JsonResponse({'success': False, 'data': form_html}) 
        # Redirect to a URL or view name


def Ajax_ShowCompanyModal(request):
    if request.method == 'POST':
        print("post")
    else:
        form = ContractorForm()
        form_html = render(request, 'polls/ajax_company.html', {'form': form}).content.decode('utf-8')
        return JsonResponse({'success': True, 'data': form_html})
    
def SaveCompanyinfo(request):
    if request.method == 'POST':
        form = ContractorForm(request.POST)
        if form.is_valid():
            new_company= form.save()
            return JsonResponse({'success': True,'id': new_company.id, 'name': new_company.Company_Name, 'data':'form submitted'})
        else:
            form_html = render(request, 'polls/ajax_company.html', {'form': form}).content.decode('utf-8')
            return JsonResponse({'success': False, 'data': form_html})
        



@login_required       
def add_category(request):
    if request.method=="POST":
        form=Fa_CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"added sccesfully")
            return redirect('polls:View_category')
        else:
            return render(request,'polls/fa_category_technology.html',{'form': form})

    else:

        form=Fa_CategoryForm()
        categoy_obj = Fa_Category.objects.all()
        context= {'form': form,
                  'categoy_obj':categoy_obj
                  }


        return render(request,'polls/fa_category_technology.html',context)
    
@login_required  
def add_sub_category(request):
    if request.method=="POST":
        form=Fa_SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"added sccesfully")
            return redirect('polls:View_category')
        else:
            return render(request,'polls/fa_category_technology.html',{'form': form})

    else:

        form=Fa_SubCategoryForm()
        categoy_obj = Fa_Category.objects.all()
        context= {'form': form,
                  'categoy_obj':categoy_obj
                  }


        return render(request,'polls/fa_category_technology.html',context)
    
#dont add decorator @login required with ajax.  
def View_category(request):
    if request.method=="POST":
        print("post")
    else:
        categoy_obj = Fa_Category.objects.all()
        context= {
                  'categoy_obj':categoy_obj
                  }


        return render(request,'polls/fa_View_category.html',context)

@login_required
def View_category(request):
    if request.method=="POST":
        print("post")
    else:
        categoy_obj = Fa_Category.objects.all()
        context= {
                  'categoy_obj':categoy_obj
                  }


        return render(request,'polls/fa_View_category.html',context)
    
#dont add decorator @login required with ajax.    
def get_subcategories(request, category_id):
    

    subcategories = Fa_SubCategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)

@login_required
def add_Fa_contracts(request):
    if request.method=="POST":
        form=Fa_ContractForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"New Contract has been added sccesfully")
            #return render(request,'polls/fa_contracts.html',{'form': form})
            return redirect('polls:ContractsView')
        else:
            return render(request,'polls/fa_contracts.html',{'form': form})

    else:
        form=Fa_ContractForm()
       
        context= {'form': form,
                  
                  }
        return render(request,'polls/fa_contracts.html',context)
    
@login_required
def ContractsView(request):

    if request.method=="POST":
        print("post")
    else:
        contracts_obj = Fa_Contract.objects.all()

        context= {
                  'contracts_obj':contracts_obj
                  }
        return render(request,'polls/fa_Display_contracts.html',context)
    

@login_required    
def Add_Vendor(request):
    if request.method == 'POST':
        form = ContractorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:Add_Vendor')
        else:
            return render(request, 'polls/fa_add_vendor.html', {'form': form})
            
    else:
        form = ContractorForm()
        vendor_obj =Contractor.objects.all()
        context={'form': form,
                 'vendor_obj':vendor_obj
                 }
        return  render(request, 'polls/fa_add_vendor.html', context)

@login_required
def IssuePM(request):
   
    if request.method=="POST":
        form=Fa_PMForm(request.POST)
        station_name= request.POST.get('station_name') 
       
        if form.is_valid():
                station = get_object_or_404(Station, pk=station_name)
                work_order = Workorder.objects.create(
                    Created_By=request.user,
                    Type_of_work=1 ,
                    station_name=station 
                 )
                
                instance= form.save(commit=False)
                instance.Created_By = request.user
                instance.work_order=work_order

                contract_frequency = instance.contract.frequency
                if contract_frequency == 1:  # Monthly
                    next_pm_date = timezone.now().date() + timedelta(days=30)
                elif contract_frequency == 2:  # Quarterly
                    next_pm_date = timezone.now().date() + timedelta(days=90)
                elif contract_frequency == 3:  # Quarterly
                    next_pm_date = timezone.now().date() + timedelta(days=60)
                elif contract_frequency == 4:  # Quarterly
                    next_pm_date = timezone.now().date()  + timedelta(days=60)
                else:
                    next_pm_date = timezone.now().date()  + timedelta(days=15)
             
                instance.next_pm_date = next_pm_date

                instance.save()
                work_order.PM_order=instance
                work_order.save()
        
                pm_obj = PreventiveMaintenance.objects.filter(id=instance.id)
                context= {
                        'pm_obj':pm_obj
                        }
                messages.success(request, "Preventive Mantanence WOrk Order issued successfully.Reference number is :" + str(work_order.id))
                return render(request,'polls/fa_Display_PM.html',context)      
        else:
             
            context={
            'form':form
            }

            return render (request,'polls/fa_CreateWorkOrder.html',context)

    else:
    
        form=Fa_PMForm()

        context={
            'form':form
        }

        return render (request,'polls/fa_CreateWorkOrder.html',context)

@login_required
def PMView(request):

    if request.method=="POST":
        print("post")
    else:
        pm_obj = PreventiveMaintenance.objects.all()
        context= {
                  'pm_obj':pm_obj
                  }
        return render(request,'polls/fa_Display_PM.html',context)
    

@login_required
def IssueCM(request):
   
    if request.method=="POST":
        form=Fa_CMForm(request.POST)
        station_name= request.POST.get('station_name') 
        
       
        if form.is_valid():
            station = get_object_or_404(Station, pk=station_name)
            work_order = Workorder.objects.create(
                    Created_By=request.user,
                    Type_of_work=2 ,
                    station_name=station 
                 )
                
            instance= form.save(commit=False)
            instance.Created_By = request.user
            instance.work_order=work_order
            instance.save()
            form.save_m2m() 
            work_order.CM_order=instance
            work_order.save()
            cm_obj = CorrectiveMaintenance.objects.filter(id=instance.id)
            
            context= {
                        'cm_obj':cm_obj
                        }
            messages.success(request, "Corrective Mantanence Work Order issued successfully.Reference number is :" + str(work_order.id))
            return render(request,'polls/fa_Display_CM.html',context)      
            #return redirect('polls:CMView')
        else:
            context={
            'form':form
            }

            return render (request,'polls/fa_Issue_CM.html',context)

    else:
       
        
        
        form=Fa_CMForm()

        context={
            'form':form
        }

        return render (request,'polls/fa_Issue_CM.html',context)

@login_required   
def CMView(request):

    if request.method=="POST":
        print("post")
    else:
        cm_obj = CorrectiveMaintenance.objects.all()
        context= {
                  'cm_obj':cm_obj
                  }
        return render(request,'polls/fa_Display_CM.html',context)  
    

@login_required
def issue_new_maintenance(request):
    if request.method == 'POST':
        form = Fa_NewWorkForm(request.POST)
        station_name= request.POST.get('station_name') 
        
        if form.is_valid():
            station = get_object_or_404(Station, pk=station_name)
            work_order = Workorder.objects.create(
                    Created_By=request.user,
                    Type_of_work=3 ,
                    station_name=station 
                 )
            instance= form.save(commit=False)
            instance.created_by = request.user
            instance.work_order=work_order
            instance.save()
            form.save_m2m() 
            work_order.CM_order=instance
            work_order.save()
            New_Obj = NewMaintanence.objects.filter(id=instance.id)
            
            context= {
                        'New_Obj':New_Obj
                        }
            messages.success(request, "New Mantanence  Order issued successfully.Reference number is :" + str(work_order.id))
            return render(request,'polls/fa_Display_New_Maintanence.html',context) 
            
           
    else:
        form = Fa_NewWorkForm()

    return render(request, 'polls/fa_Issue_New_Maintanence.html', {'form': form})

@login_required   
def NewWorkOrderView(request):

    if request.method=="POST":
        print("post")
    else:
        New_Obj = NewMaintanence.objects.all()
        context= {
                  'New_Obj':New_Obj
                  }
        return render(request,'polls/fa_Display_New_Maintanence.html',context)  
    

#dont add decorator @login required with ajax.
def get_contract_details(request):
    contract_id = request.GET.get('contract_id')
  
    contract = get_object_or_404(Fa_Contract, id=contract_id)
    
    data = {
        'contractor': contract.contractor.id if contract.contractor else None,
        'category': contract.category.id if contract.category else None,
        'subcategories': list(contract.subcategory.values('id', 'name')),  # Assuming subcategory has a 'name' field
    }
   
   
    return JsonResponse(data)

@login_required   
def DetailContractsView(request,id):
   
    contracts_obj = Fa_Contract.objects.prefetch_related('Fa_ContractFile').get(id=id)
    Preventivemaint_obj =PreventiveMaintenance.objects.filter(contract=contracts_obj)
    Correctivemaint_obj =CorrectiveMaintenance.objects.filter(contract=contracts_obj)
    Newmaint_obj =NewMaintanence.objects.filter(contract=contracts_obj)
    
   
  
    if request.method=="POST":
        form=Fa_FileuploadForm(request.POST,request.FILES)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.Created_By =request.user
            instance.contract =contracts_obj
            instance.save()  
            return redirect('polls:DetailContractsView',id=contracts_obj.id)
        else:
            context= {
            'form': form,
            'obj':contracts_obj
                  }
            return render(request,'polls/fa_contractsDetailView.html',context)

    else:
        form=Fa_FileuploadForm()
        pmfileuploadform= Fa_PMFileuploadForm()
        PMCommentform =PMCommentForm()
        cmfileuploadform= Fa_CMFileuploadForm()
        CMCommentform =CMCommentForm()
        NewCommentform= NewCommentForm()
        Newfileuploadform =Fa_NewFileuploadForm()
        context= {
            'form': form,
            'obj':contracts_obj,
            'Preventivemaint_obj':Preventivemaint_obj,
            'Correctivemaint_obj': Correctivemaint_obj,
             'Newmaint_obj' : Newmaint_obj,
            'pmfileuploadform':pmfileuploadform,
            'PMCommentform':PMCommentform,
             'Fa_CMFileuploadForm' :cmfileuploadform,
             'CMCommentForm' : CMCommentform,
             'NewCommentForm' : NewCommentform,
            'Fa_NewFileuploadForm' :Newfileuploadform,
            
           
                  }
        return render(request,'polls/fa_contractsDetailView.html',context)


#dont add decorator @login required with ajax.
def uploadpmfiles(request):
    if request.user.is_authenticated:
        if request.method== "POST":
            
            form= Fa_PMFileuploadForm(request.POST,request.FILES)
        
            pmid = request.POST.get('pmid')
        
            if form.is_valid():
                pm_instance = PreventiveMaintenance.objects.get(id=pmid)
                instance=form.save(commit=False)
                instance.pm= pm_instance
                instance.Created_By=request.user
                instance.save()
                created_by=f"{instance.Created_By.first_name} {instance.Created_By.last_name}"
                file_info = {
                    'success': True,
                    'pm_id': pm_instance.id,
                    'Created_By': created_by,
                    'uploaded_at': instance.uploaded_at,
                    'file_url': instance.file.url,
                    'filename': instance.filename
                }
            
                return JsonResponse(file_info)
            else:
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        else:
            return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
    else:
        return JsonResponse({'success': False, 'message': 'User is not authenticated.please login first'})
            
    
 #upload using ajax

#dont add decorator @login required with ajax.
def uploadcmfiles(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Fa_CMFileuploadForm(request.POST, request.FILES)
            cm_file_id = request.POST.get('cm_file_id')
            if form.is_valid():
                cm_instance = get_object_or_404(CorrectiveMaintenance, id=cm_file_id)
                instance = form.save(commit=False)
                instance.cm = cm_instance
                instance.Created_By=request.user
                instance.save()
                created_by=f"{instance.Created_By.first_name} {instance.Created_By.last_name}"
                file_info = {
                    'success': True,
                    'cm_id': cm_instance.id,
                    'Created_By': created_by,
                    'uploaded_at': instance.uploaded_at,
                    'file_url': instance.file.url,
                    'filename': instance.filename
                }
            
                return JsonResponse(file_info)
            else:
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        else:
            return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
    else:
        return JsonResponse({'success': False, 'message': 'User is not authenticated.please login first'})


#upload using ajax

#dont add decorator @login required with ajax.
def uploadnewfiles(request):
   
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Fa_NewFileuploadForm(request.POST, request.FILES)
            new_file_id = request.POST.get('new_file_id')
           
            if form.is_valid():
                new_instance = get_object_or_404(NewMaintanence, id=new_file_id)
                instance = form.save(commit=False)
                instance.New = new_instance
                instance.Created_By=request.user
                instance.save()
                created_by=f"{instance.Created_By.first_name} {instance.Created_By.last_name}"
                file_info = {
                    'success': True,
                    'cm_id': new_instance.id,
                    'Created_By': created_by,
                    'uploaded_at': instance.uploaded_at,
                    'file_url': instance.file.url,
                    'filename': instance.filename
                }
            
                return JsonResponse(file_info)
            else:
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        else:
            return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
    else:
        return JsonResponse({'success': False, 'message': 'User is not authenticated.please login first'})





def uploadnewfiles_htmx(request):
    print("View was triggered") 
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Fa_NewFileuploadForm(request.POST, request.FILES)
            new_file_id = request.POST.get('new_file_id')
           
            if form.is_valid():
                new_instance = get_object_or_404(NewMaintanence, id=new_file_id)
                instance = form.save(commit=False)
                instance.New = new_instance
                instance.Created_By=request.user
                instance.save()
                
            
                return HttpResponse(
                    f'''
                    <tr>
                        <td>{ instance.Created_By }</td>
                        <td>{ instance.uploaded_at.strftime('%Y-%m-%d %H:%M:%S') }</td>
                        <td><a href="{ instance.file.url }" target="_blank">{ instance.filename }</a></td>
                    </tr>
                    '''
                )
            else:
                return HttpResponse("Invalid", status=400)
        else:
            return HttpResponse("Invalid", status=400)
    else:   
        response = JsonResponse({})
        response['HX-Trigger'] = json.dumps({
                    "show-toast": {
                        "level": "error",
                        "title": "Failed",
                        "message": "User is not authenticated.please login first!"
                    }
                })
        return response 
        #return HttpResponse('User is not authenticated.please login first')

#dont add decorator @login required with ajax.
def add_comment(request):
    if request.user.is_authenticated:
        comment_form = PMCommentForm(request.POST)
        if comment_form.is_valid():
            pm_record_id = request.POST.get('pm_record_id')
            pm_record = get_object_or_404(PreventiveMaintenance, pk=pm_record_id)
            new_comment = comment_form.save(commit=False)
            new_comment.pm_record = pm_record
            new_comment.user = request.user
            new_comment.save()
            comment_data = {
            'user': new_comment.user.username,
            'text': new_comment.text,
            'pm': new_comment.pm_record_id,
            'created_at': new_comment.created_at
            }
            return JsonResponse({'success': True, 'comment': comment_data})
        else:
            return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': False, 'message': 'User is not authenticated.please login first'})
        
        
#dont add decorator @login required with ajax.
def add_CM_comment(request):
    if request.user.is_authenticated:
        comment_form = CMCommentForm(request.POST)
        if comment_form.is_valid():
            cm_record_id = request.POST.get('cm_record_id')
            cm_record = get_object_or_404(CorrectiveMaintenance, pk=cm_record_id)
            new_comment = comment_form.save(commit=False)
            new_comment.cm_record = cm_record
            new_comment.user = request.user
            new_comment.save()
            comment_data = {
            'user': new_comment.user.username,
            'text': new_comment.text,
            'cm': new_comment.cm_record_id,
            'created_at': new_comment.created_at
            }
            return JsonResponse({'success': True, 'comment': comment_data})
        else:
            return JsonResponse({'success': False})
    else:
        return HttpResponse({'success': False, 'message': 'User is not authenticated.please login first'})
    
    
#dont add decorator @login required with ajax.
def add_Newwork_comment(request):
    if request.user.is_authenticated:
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            New_record_id = request.POST.get('New_record_id')
            New_record = get_object_or_404(NewMaintanence, pk=New_record_id)
            new_comment = comment_form.save(commit=False)
            new_comment.New_record = New_record
            new_comment.user = request.user
            new_comment.save()
            comment_data = {
            'user': new_comment.user.username,
            'text': new_comment.text,
            'cm': new_comment.New_record_id,
            'created_at': new_comment.created_at
            }
            
      
            return JsonResponse({'success': True, 'comment': comment_data})
        else:
            return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': False, 'message': 'User is not authenticated.please login first'})



def add_NewWork_comment_htmx(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = NewCommentForm(request.POST)
            if form.is_valid():
                New_record_id = request.POST.get('New_record_id')
                New_record = get_object_or_404(NewMaintanence, pk=New_record_id)
                new_comment = form.save(commit=False)
                new_comment.New_record = New_record
                new_comment.user = request.user  # Set the user
                new_comment.save()
                new_row_html = render_to_string('polls/fa_partial_new_comments.html', {'file': new_comment})
                response = HttpResponse(new_row_html, content_type="text/html")
                
                response['HX-Trigger'] = json.dumps({
                    "show-toast": {
                        "level": "success",
                        "title": "Success",
                        "message": "Comment Added successfully!"
                    }
                })
                return response 
                
            else:
                # Return an error message for invalid form
                return HttpResponse("Invalid comment", status=400)
            
    return HttpResponse('Invalid comment', status=400)


        
@login_required
def WorkOrderView(request):

    if request.method=="POST":
        print("post")
    else:
       # workorder_obj = Workorder.objects.all()
        workorder_obj=Workorder.objects.all().select_related('preventivemaintenance')

        context= {
                  'workorder_obj':workorder_obj
                  }
        
        return render(request,'polls/fa_Display_WorkOrder.html',context)

@login_required    
def Detail_Work_Order_View(request,id):
    
    Work_order_obj = Workorder.objects.get(id=id)
    Preventivemaint_obj =PreventiveMaintenance.objects.filter(work_order=Work_order_obj)
    Correctivemaint_obj =CorrectiveMaintenance.objects.filter(work_order=Work_order_obj)
    Newmaint_obj =NewMaintanence.objects.filter(work_order=Work_order_obj)
    workpermit_obj = Workpermit.objects.filter(work_order=id)
    
   
  
    if request.method=="POST":
        print("post")

    else:

        pmfileuploadform= Fa_PMFileuploadForm()
        PMCommentform =PMCommentForm()
        cmfileuploadform= Fa_CMFileuploadForm()
        CMCommentform =CMCommentForm()
        NewCommentform= NewCommentForm()
        Newfileuploadform =Fa_NewFileuploadForm()
        
        context= {
            
            'obj':Work_order_obj,
            'Preventivemaint_obj':Preventivemaint_obj,
            'Correctivemaint_obj': Correctivemaint_obj,
            'Newmaint_obj' : Newmaint_obj,
            'workpermit_obj': workpermit_obj,
            'pmfileuploadform':pmfileuploadform,
            'PMCommentform':PMCommentform,
            'Fa_CMFileuploadForm' :cmfileuploadform,
            'CMCommentForm' : CMCommentform,
            'NewCommentForm' : NewCommentform,
            'Fa_NewFileuploadForm' :Newfileuploadform,
            
           
           
                  }
        return render(request,'polls/fa_Work_Order_DetailView.html',context)

@login_required
def Create_WorkPermit_PM(request,id):
    pm_record = get_object_or_404(PreventiveMaintenance, work_order=id)
    if request.method == "POST":
        form =PM_WorkPermitForm(request.POST,obj=pm_record)
        if form.is_valid():
            instance=form.save()
            ref_obj = instance.id
            
            messages.success(request,' YOUR WORKPERMIT saved successfully. REF NO IS : ' + str(ref_obj)+ '. Please save the reference number for future reference')
            return redirect('polls:displayworkpermits')
        else:
            return render(request,'polls/fa_Workpermit_PM.html', {'form': form})
    else:
        form =PM_WorkPermitForm(obj=pm_record)
        return render(request,'polls/fa_Workpermit_PM.html', {'form': form})
        
@login_required
def Create_WorkPermit_CM(request,id):
    print('Ajmal')
    print(id)
   # wo_record = get_object_or_404(Workorder, pk=id)
    cm_record=get_object_or_404(CorrectiveMaintenance, work_order=id)
    print(cm_record)
    if request.method == "POST":
        form =CM_WorkPermitForm(request.POST,obj=cm_record)
        if form.is_valid():
            instance=form.save()
            ref_obj = instance.id
            
            messages.success(request,' YOUR WORKPERMIT saved successfully. REF NO IS : ' + str(ref_obj)+ '. Please save the reference number for future reference')
            return redirect('polls:displayworkpermits')
        else:
            return render(request,'polls/fa_Workpermit_PM.html', {'form': form})
    else:
        form =CM_WorkPermitForm(obj=cm_record)
        return render(request,'polls/fa_Workpermit_PM.html', {'form': form}) 
    

@login_required
def Create_WorkPermit_NewWork(request,id):
    print('Ajmal')
    print(id)
   # wo_record = get_object_or_404(Workorder, pk=id)
    new_record=get_object_or_404(NewMaintanence, work_order=id)
    print(new_record)
    if request.method == "POST":
        form =New_WorkPermitForm(request.POST,obj=new_record)
        if form.is_valid():
            instance=form.save()
            ref_obj = instance.id
            
            messages.success(request,' YOUR WORKPERMIT saved successfully. REF NO IS : ' + str(ref_obj)+ '. Please save the reference number for future reference')
            return redirect('polls:displayworkpermits')
        else:
            return render(request,'polls/fa_Workpermit_PM.html', {'form': form})
    else:
        form =New_WorkPermitForm(obj=new_record)
        return render(request,'polls/fa_Workpermit_PM.html', {'form': form}) 


def calendar_events(request):
    # Fetch or modify events in the database depending on the HTTP method
    contracts = Fa_Contract.objects.all()
    pm_obj= PreventiveMaintenance.objects.all()
    
    events = []
    for contract in contracts:
        # Add contract expiry events
            if contract.end_date:
                events.append({
                    'title': f'Contract Expiry: {contract.contract_reference_number}',
                    'start': contract.end_date.isoformat(),
                    'allDay': True,
                    'color': '#ff6347',
                })

            last_pm = contract.preventivemaintenance_set.order_by('-uploaded_at').first()
           
            if last_pm and last_pm.uploaded_at:
            # Calculate the next PM date based on the frequency defined in the contract
                if contract.frequency == 1:  # Monthly
                    next_pm_date = last_pm.uploaded_at + timedelta(days=30)
                elif contract.frequency == 2:  # Quarterly
                    next_pm_date = last_pm.uploaded_at + timedelta(days=90)
                elif contract.frequency == 3:  # Quarterly
                    next_pm_date = last_pm.uploaded_at + timedelta(days=60)
                elif contract.frequency == 4:  # Quarterly
                    next_pm_date = last_pm.uploaded_at + timedelta(days=60)
                else:
                    next_pm_date = last_pm.uploaded_at + timedelta(days=15)


                events.append({
                    'title': f'PM:{contract.contractor}',
                    'start': next_pm_date.isoformat(),
                    'allDay': True,
                    'color': '#6495ed',  # Different color to distinguish PM events
                })

    return JsonResponse(events, safe=False)

def displayevents(request):
    if request.method=="POST":
        print('POST')

    else:
        return render(request,'polls/fa_Display_Events.html')
       

def filter_petty_workpermits(request):

    form=WorkPermitFilterForm()
    filters = {}
    for key, value in request.GET.items():
        if value:
            filters[key] = value

    start_date_str = filters.get('Start_date')
    end_date_str = filters.get('End_date')
    station_name = filters.get('station_name') 
    Contracting_Company_Name = filters.get('Contracting_Company_Name') 

    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None
    except ValueError:
    # Handle invalid date format
        start_date = None
        end_date = None

    query_filters = Q()
    if start_date:
        query_filters &= Q(created_date__gte=start_date)
    if end_date:
        query_filters &= Q(created_date__lte=end_date)
    if station_name:
        query_filters &= Q(station_name=station_name)
    if Contracting_Company_Name:
        query_filters &= Q(Contracting_Company_Name=Contracting_Company_Name)

        print(query_filters)

    WorkPermit_requests = Workpermit.objects.filter(query_filters)
    

    if not WorkPermit_requests:
        messages.error(request, 'You dont have any requests to show',extra_tags='info')
    
    return render(request,'polls/WorkpermitView.html',{'obj' : WorkPermit_requests,'form':form})