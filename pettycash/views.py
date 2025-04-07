import http
from io import BytesIO
from logging import warning
from math import exp
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from numpy import info

from myproject.context_processors import group_required
from .forms import ExpenseFilterForm, ExpenseForm, ExpenseItemFormSet, Travelclaims, TravelclaimForm, travelclaiminfo
from .models import Expense,CustomUser, ExpenseItem, TravelClaim
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Sum
from django.views.generic.edit import (
    CreateView, UpdateView
)
from django.core.signing import TimestampSigner, SignatureExpired, BadSignature
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from django.core.signing import TimestampSigner
import datetime
from django.db.models import Q
import io
import os
from django import forms
from reportlab.lib.colors import HexColor
from datetime import datetime
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle




def home(request):
    if request.method =="POST":
        print("post")
    else:
        return render(request,'financehomepage.html')
    

def pdfgenerate(id):
    
    expense = Expense.objects.select_related('employee').filter(id=id)
    
    Expense_Items = ExpenseItem.objects.select_related('expense').filter(expense=id)
    
    buffer = BytesIO()

    c = canvas.Canvas(buffer,pagesize=A4)
    
    # Draw Main Heading border
    grey_value=0.5
    hex_color = colors.HexColor("#E5E4E2")
    c.setStrokeColorRGB(grey_value, grey_value, grey_value)
    c.rect(32, A4[1]-90, width=142, height=60)
    c.rect(176, A4[1]-90, width=242, height=60)
    c.rect(420, A4[1]-90, width=144, height=60)# Draw a rectangle (x, y, width, height)

    
    # Set font and size for Main heading
    c.setFont("Helvetica-Bold", 14)
    #c.setStrokeColorRGB(0.647, 0.165, 0.165)
    c.setStrokeColorRGB(0, 0, 0)
    for value in expense:
        if value.total_amount <= 499:
            c.drawString(230, A4[1] - 70, "Claim Form")
        else:
            c.drawString(230, A4[1] - 70, "Claim Form")
        
    
    
    # Draw the title
    c.setFont("Helvetica", 8)
    grey_value = 0.5  
    c.setFillColorRGB(grey_value, grey_value, grey_value)
    c.drawString(40, A4[1] - 60, "SATS/KSA/FM/K/001")

    # Set font for invoice details & ITEMS
    c.setFont("Helvetica", 12)
    
      #Add SATS LOGO
        
    image_path = finders.find('satsksa.png')
    watermark_path = finders.find('satsgroupcmyk.png')
    
    if image_path:
        c.drawImage(image_path, x=443, y=A4[1] - 85, width=90, height=50)
    
    # Add other fields as needed
    
    Common_starting_height = A4[1] - 200 
    
    margin = 30  # 1 inch margin (72 points per inch)
    border_width = 2  # Set the border width
    gap=2
    line_width = 0.5
    
    # Draw a multiline  border around the entire page
    
    for i in range(border_width):
        c.setLineWidth(line_width)
        c.rect(margin - i * gap, margin - i * gap, A4[0] - 2 * (margin - i * gap), A4[1] - 2 * (margin - i * gap), stroke=1)

    

#Header Table

# Write Checklist details  
    common_detail_xaxis= 50 
    
    
    
    data = []
    
    for value in expense:
        formatted_date = value.date.strftime('%d-%b-%Y')
        description = value.description
        First_Name = value.employee.first_name
        Last_Name = value.employee.last_name
        Totalamount= value.total_amount
        Notes = value.description if value.description else ''

    if Totalamount <= 499:
        row = [
        [f"CLAIM REF NO",'',value.id,f"PCV NO",'',],
        [f"Station",f"{value.employee.station_name}",f"Claimant", f"{value.claimant}",f"Created Date", formatted_date],
        
        
        ] 
    else:
        row = [
        [f"CLAIM REF NO",'',value.id,f"REF NO",'',],
        [f"Station",f"{value.employee.station_name}",f"Claimant", f"{value.claimant}",f"Created Date", formatted_date],
        
        
        ] 
    data.extend(row)   
    row_height = 30
    
    col_widths = [60,60,84,115,84,83]
    
        
    Common_table = Table(data,rowHeights=row_height,colWidths=col_widths)
    Common_table.setStyle(TableStyle([
        
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),  # Add borders to all cells
        
        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Align content to center
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font bold
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical alignment to middle
        ('SPAN', (0, 0), (1, 0)),
        ('SPAN', (4, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (1, 0),  hex_color),
        ('BACKGROUND', (3, 0), (3, 0), hex_color),
        ('BACKGROUND', (0, 1), (0, 1), hex_color),
        ('BACKGROUND', (2, 1), (2, 1), hex_color),
         ('BACKGROUND', (4, 1), (4, 1), hex_color),
        
       
    ]))  
    
    
    Common_table.wrapOn(c, A4[0], A4[1])
    Common_table.drawOn(c, common_detail_xaxis, Common_starting_height)
    
    
    #item table
    
    start_y=220
    start_x = 50  # X-coordinate
    start_height = A4[1] - start_y # Initial Y-coordinate
   
    
    data = [
        [f"SL No",f"Item description",f"Quantity",f"Unit Price",f"Amount" ,]
        ] 

    for index, item in enumerate(Expense_Items, start=1):
        data.append([str(index), item.item_name, str(item.quantity),str(item.unit_price),str(item.amount)])
        
    Total_Amount_Row = [
          ["Total Amount","","","",f"{Totalamount} SAR"]
        
    ]
    data.extend(Total_Amount_Row)  

    #table = Table(data)
    style= TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), hex_color),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Default gridlines for all cells
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.black),  # Header line weight (thicker)
        ('TOPPADDING', (0, 0), (-1, -1), 4),  # Adding padding to separate lines
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),  
        ('SPAN', (0, -1), (-2, -1)),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#a61f38")),
        ('TEXTCOLOR', (0, -1), (-1, -1), colors.white), 
        ('ROWHEIGHT', (0, 0), (-1, -1), 54),
        ('FONTSIZE', (0, 0), (-1, -1), 8), 
        
        ])
    
    col_widths= [40, 200, 80,80,90]
    table = Table(data, col_widths)
    table.setStyle(style)
    
    row_count = len(data)
    start_y = start_y + (20 *row_count-1)
    table.wrapOn(c, A4[0], A4[1])
    table.drawOn(c, start_x, A4[1] - start_y)

     ####Table for acknowledgment 
    data = [
        ["NOTES*",Notes,""],
        ["",f"Prepared by",f"Certified By",f"Approved By",f"Recived" ],
        [f"Name","","","",""],
        [f"Signature","","","",""]
        ]
    style= TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), hex_color),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Default gridlines for all cells
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.black),  # Header line weight (thicker)
        ('TOPPADDING', (0, 0), (-1, -1), 4),  # Adding padding to separate lines
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),  
        ('SPAN', (1, 0), (4, 0)),
        ('FONTSIZE', (0, 0), (-1, 1), 8),   
        #('WORDWRAP', (0, 0), (0, -1)),
        ('VALIGN', (0, 0), (0, -1), 'MIDDLE'),
    
        ])
    uniform_column_width = 102
    table = Table(data,colWidths=uniform_column_width)
    
    row_heights = [20, 20,50]  # None for the header row, 40 for the second row

# Set row heights for the table
    table._argH[1:] = row_heights 
    table.setStyle(style)
    table_starting_height = A4[1] -590
    table.wrapOn(c, A4[0], A4[1])
    table.drawOn(c, 42, table_starting_height)
        
    #########For accounts purpose only
    first_row = ['ACCOUNTS DEPARTMENT USE ONLY ']* 16
    second_row = [
        "ACCOUNT","","","","","CENTRE","","","","", "CROSS REFERENCE", "PROJECT CODE",
        "CODE", "AMOUNT","", "ID"
    ]
    third_row = [''] * 16  # Creating an empty row with 16 columns
    data = [first_row, second_row, third_row]
    
    for _ in range(8):
        data.append([''] * 8)

    # Define table style
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), hex_color),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 1), (-1, 1), 8),     
        # Color for the spanned row
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),      # Text color for the spanned row
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),             # Alignment for all cells
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),            # Vertical alignment for all cells
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),  # Grid lines
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('SPAN', (0, 0), (15, 0)),
        ('SPAN', (0, 1), (4, 1)),
        ('SPAN', (5, 1), (9, 1)),
        ('SPAN', (13, 1), (14, 1)),
        ('WORDWRAP', (0, 0), (-1, -1)),
        
         
    ])

    col_widths = [15] * 16  # Column widths for the table
    col_widths[10:10] = [110] * 2
    col_widths[11] = 90
    col_widths[12] = 50
    col_widths[13] = 40
    col_widths[14] = 30
    col_widths[15] = 40
    
    table = Table(data, colWidths=col_widths)
    # Create table object and apply style
    #table = Table(data)
    table.setStyle(style)
    table_starting_height = A4[1] -800
    table.wrapOn(c, A4[0], A4[1])
    table.drawOn(c, 42, table_starting_height)

  
    c.showPage()
    c.save()
    #buffer.seek(0)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    
    
    return pdf_bytes
    
    
    """ shared_folder_path = '//192.168.1.110/facility dmm/Work permit/'
    
    today_date = datetime.now().strftime('%Y%m%d')
    
    shared_file_name = f'{today_date}_{value.id}_01.pdf'
    shared_file_path = os.path.join(shared_folder_path, shared_file_name)
    count = 1
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{shared_file_name}"'
    while os.path.exists(shared_file_path):
        # Append a suffix to the file name if it already exists
        count += 1
        shared_file_name = f'{today_date}_{value.id}_{count:02d}.pdf'
        shared_file_path = os.path.join(shared_folder_path, shared_file_name)
        response['Content-Disposition'] = f'attachment; filename="{shared_file_name}"'
     
    with open(shared_file_path, 'wb') as pdf_file:
        pdf_file.write(pdf_bytes) """ 

    #for downloading the PDF
    
    """ 
    context={
        
        'response' :response,# to download the pdf
        #'filepath' :shared_file_path,
        
        #'buffer': pdf_bytes # to show the content of pdf in iframe.iframe must be defined inside html template
    }
        return context
 """


@login_required
def TravelClaimcreate(request):
    
    if request.method =='POST':
         claimant = request.POST.get('Claimant')
         staff_ID = request.user.employee_id
         Station = request.POST.get('station_name')
         if Station == '3':
                Station_value="JED"
         elif Station == '2' :
                Station_value= "RUH"
         else:
            
             Station_value="DMM"
         
         Start_date = request.POST.get('Start_date')
         End_date = request.POST.get('End_date')
         Days = request.POST.get('Days')
         justification = request.POST.get('justification')
         
         Accomdation = request.POST.get('Accomdation')
         Meals = request.POST.get('Meals')
         Transportation = request.POST.get('Transportation')
         miscellaneous = request.POST.get('miscellaneous')
         Total = int(Accomdation) + int(Meals)+ int(Transportation)+ int(miscellaneous)
        
         buffer = BytesIO()
         
         pdf = canvas.Canvas(buffer, pagesize=A4)
         elements = []
         grey_value = 0.5
         hex_color = colors.HexColor("#E5E4E2")
         pdf.setStrokeColorRGB(grey_value, grey_value, grey_value)
         pdf.rect(32, A4[1]-90, width=142, height=60)
         pdf.rect(176, A4[1]-90, width=242, height=60)
         pdf.rect(420, A4[1]-90, width=144, height=60)# Draw a rectangle (x, y, width, height)

    
    # Set font and size for Main heading
         pdf.setFont("Helvetica-Bold", 14)
    #c.setStrokeColorRGB(0.647, 0.165, 0.165)
         pdf.setStrokeColorRGB(0, 0, 0)
         pdf.drawString(230, A4[1] - 70, "Travel Claim Form")
      
    # Draw the title
         pdf.setFont("Helvetica", 8)
         grey_value = 0.5  
         pdf.setFillColorRGB(grey_value, grey_value, grey_value)
         pdf.drawString(40, A4[1] - 60, "SATS/KSA/FM/K/001")

        # Set font for invoice details & ITEMS
         pdf.setFont("Helvetica", 12)
    
      #Add SATS LOGO
        
         image_path = finders.find('sats Saudi arabia.jpg')
    
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


            data = [
            ["Claimant","", claimant,'Staff ID' ,staff_ID,'Designation',''],
            ['Start Date',"",Start_date,'End Date',End_date,'Days ',Days],
            ['Justification', "",justification,"",""],
            ["", "","","","",""],
            ['Claims',"","","","Foreign Currency","Exchange Rate","Local Currency"],
            ["",'Accommodation',"","","","", Accomdation+ ' SAR'],
            ["",'Meals',"","","","", Meals +' SAR'],
            ["",'Transportation',"","","","", Transportation +' SAR'],
            ["",'Other',"","","","", miscellaneous +' SAR'],
         
            ]
            row=["","","","","","",""]
            
            for i in range(3):
                data.append(row)
                
            new_row12 = ["Total","", "", "", "", "", str(Total) + ' SAR']
            new_row13 = ["","","","","Foreign Currency","Exchange Rate","Local Currency"]
            new_row14 = ["Advanced recieved for above travel(State Nil of no advance taken)","","","","","",""]
            new_row15 = ["Refund to company after above travel"]
            new_row16 = ["" ]
            new_row17 = [f"Name & Signature","",f"Claimant",f"Reporting Manager","",f"Approved by PCEO/EVP/SVP","" ]
            new_row18 = ["" ]
            new_row19 = ["DATE" ]
                        
                            

# Insert the new row at the 11th index (index 10 because indexing starts from 0)
            col_widths= [30,50,100, 80 ,80,80,80]
            data.insert(12, new_row12)
            data.insert(13, new_row13)
            data.insert(14, new_row14)
            data.insert(15, new_row15)
            data.insert(16, new_row16)
            data.insert(17, new_row17)
            data.insert(18, new_row18)
            data.insert(19, new_row19)

            
            row_heights = [None] * len(data)
            row_heights[0] = 40 
            row_heights[1] = 40
            row_heights[2] = 50
            row_heights[3] = 8
            row_heights[4] = 30
            row_heights[12] = 30 
            row_heights[13] = 40 
            row_heights[14] = 30
           
            row_heights[16] = 30
            row_heights[17] = 20
            row_heights[18] = 40
            row_heights[19] = 30   
                        
         # Define table styles
            table = Table(data,colWidths=col_widths,rowHeights=row_heights)
            style = TableStyle([
            ('BACKGROUND', (0, 0), (1, 2), hex_color),
            ('BACKGROUND', (3, 0), (3, 1), hex_color),
            ('BACKGROUND', (5, 0), (5, 1), hex_color),
            #('BACKGROUND', (0, 4), (-1, 4), colors.lightslategray),
            
            # Header row background color
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header row text color
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alignment
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),  # Header row font style
            ('SPAN', (0, 0), (1, 0)),
            ('SPAN', (0, 1), (1, 1)),
            ('SPAN', (0, 2), (1, 2)),
            ('SPAN', (0, 3), (1, 3)),
            ('SPAN', (2, 2), (-1, 2)),# row 2
            ('SPAN', (0, 3), (-1, 3)),# row 3
            ('ALIGN', (0, 4), (-1, 4), 'CENTER'),
            ## Header row bottom padding
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Gridlines
                ])
           
            body_style = TableStyle([
            ('WORDWRAP', (0, 4), (-1, 4)),
            ('WORDWRAP', (0, 12), (-1, -1)),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            
            
            #('SPAN', (1, 5), (2, 5)),# row 4 
            ('SPAN', (0, 4), (3, 4)),# row 4 
            ('SPAN', (1, 5), (3, 5)),# row 5
            ('SPAN', (1, 6), (3, 6)),# row 6
            ('SPAN', (1, 7), (3, 7)),# row 7
            ('SPAN', (1, 8), (3, 8)),
            ('SPAN', (1, 9), (3, 9)),
            ('SPAN', (1, 10), (3, 10)),
            ('SPAN', (1, 11), (3,11)),
            ('FONTNAME', (0, 12), (-1, 12), 'Helvetica-Bold'),  
            ('ALIGN', (0, 12), (5, 12),'RIGHT'),
            ('SPAN', (0, 12), (5, 12)),
            ('SPAN', (0, 13), (3, 13)),
            ('SPAN', (0, 14), (3, 14)),
            ('SPAN', (0, 15), (3, 15)),
            ('SPAN', (0, 16), (-1, 16)),
            ('SPAN', (0, 17), (1, 18)),
            ('VALIGN', (0, 17), (1, 18), 'MIDDLE'),
            ('ALIGN', (0, 17), (-1, -1),'CENTER'),
            ('SPAN', (3, 17), (4, 17)),
            ('SPAN', (5, 17), (6, 17)),
            ('SPAN', (0, 18), (1, 18)),
            ('SPAN', (3, 18), (4, 18)),
            ('SPAN', (5, 18), (6, 18)),
            ('SPAN', (0, 19), (1, 19)),
             ('SPAN', (3, 19), (4, 19)),
            ('SPAN', (5, 19), (6, 19)),
           
            ])
           
                 
            
        # Create a table and apply styles
            
            
            table.setStyle(style)
            table.setStyle(body_style)
            #table.setStyle(signature_style)
            elements.append(table)
            table.wrapOn(pdf, 0, 0)
            table.drawOn(pdf, 50, 200)
            
            pdf.rect(50, 50, width=500, height=150)
            pdf.drawString(230, 100, "For Accounts Dept Use only")

            pdf.save()
            pdf_data = buffer.getvalue()
            buffer.close()
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        # Write PDF data to the response
            response.write(pdf_data)
            return response
    else:
        form = Travelclaims()
        return render(request, 'travelclaim/travelclaim.html',{ 'form':form})
    
    
def travelclaimpdf(instance):
         
         
            claimant = instance.user.first_name+' '+instance.user.last_name
            staff_ID = instance.user
            Station = instance.user.station_name
            Start_date = instance.start_date
            End_date = instance.end_date
            Days = instance.days
            justification = instance.justification
            Accomdation = instance.accommodation
            Meals = instance.meals
            Transportation = instance.transportation
            miscellaneous =instance.miscellaneous
            Total = instance.Total_Amount
            form_no =str(instance.id)
            
            buffer = BytesIO()
            
            pdf = canvas.Canvas(buffer, pagesize=A4)
            elements = []
            grey_value = 0.5
            hex_color = colors.HexColor("#E5E4E2")
            pdf.setStrokeColorRGB(grey_value, grey_value, grey_value)
            pdf.rect(32, A4[1]-90, width=142, height=60)
            pdf.rect(176, A4[1]-90, width=242, height=60)
            pdf.rect(420, A4[1]-90, width=144, height=60)# Draw a rectangle (x, y, width, height)

        
        # Set font and size for Main heading
            pdf.setFont("Helvetica-Bold", 14)
        #c.setStrokeColorRGB(0.647, 0.165, 0.165)
            pdf.setStrokeColorRGB(0, 0, 0)
            pdf.drawString(230, A4[1] - 70, "Travel Claim Form")
        
        # Draw the title
            pdf.setFont("Helvetica", 8)
            grey_value = 0.5  
            pdf.setFillColorRGB(grey_value, grey_value, grey_value)
            pdf.drawString(40, A4[1] - 60, "SATS/KSA/FM/K/001")
            pdf.drawString(40, A4[1] - 80, "Form No:"+form_no)

            # Set font for invoice details & ITEMS
            pdf.setFont("Helvetica", 12)
        
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

            
                data = [
                    ["Claimant","", claimant,'Staff ID' ,staff_ID,'Designation',''],
                    ['Start Date',"",Start_date,'End Date',End_date,'Days ',Days],
                    ['Justification', "",justification,"",""],
                    ["", "","","","",""],
                    ['Claims',"","","","Foreign Currency","Exchange Rate","Local Currency"],
                    ["",'Accommodation',"","","","", str(Accomdation)+ ' SAR'],
                    ["",'Meals',"","","","", str(Meals) +' SAR'],
                    ["",'Transportation',"","","","", str(Transportation) +' SAR'],
                    ["",'Other',"","","","", str(miscellaneous) +' SAR'],
                
                     ]
                row=["","","","","","",""]
                    
                for i in range(3):
                        data.append(row)
                        
            new_row12 = ["Total","", "", "", "", "", str(Total) + ' SAR']
            new_row13 = ["","","","","Foreign Currency","Exchange Rate","Local Currency"]
            new_row14 = ["Advanced recieved for above travel(State Nil of no advance taken)","","","","","",""]
            new_row15 = ["Refund to company after above travel"]
            new_row16 = ["" ]
            new_row17 = [f"Name & Signature","",f"Claimant",f"Reporting Manager","",f"Approved by PCEO/EVP/SVP","" ]
            new_row18 = ["" ]
            new_row19 = ["DATE" ]
            
# Insert the new row at the 11th index (index 10 because indexing starts from 0)
            col_widths= [30,50,100, 80 ,80,80,80]
            data.insert(12, new_row12)
            data.insert(13, new_row13)
            data.insert(14, new_row14)
            data.insert(15, new_row15)
            data.insert(16, new_row16)
            data.insert(17, new_row17)
            data.insert(18, new_row18)
            data.insert(19, new_row19)

            
            row_heights = [None] * len(data)
            row_heights[0] = 40 
            row_heights[1] = 40
            row_heights[2] = 50
            row_heights[3] = 8
            row_heights[4] = 30
            row_heights[12] = 30 
            row_heights[13] = 40 
            row_heights[14] = 30
           
            row_heights[16] = 30
            row_heights[17] = 20
            row_heights[18] = 40
            row_heights[19] = 30
            
            
             # Define table styles
            table = Table(data,colWidths=col_widths,rowHeights=row_heights)
            style = TableStyle([
            ('BACKGROUND', (0, 0), (1, 2), hex_color),
            ('BACKGROUND', (3, 0), (3, 1), hex_color),
            ('BACKGROUND', (5, 0), (5, 1), hex_color),
            #('BACKGROUND', (0, 4), (-1, 4), colors.lightslategray),
            
            # Header row background color
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header row text color
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alignment
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),  # Header row font style
            ('SPAN', (0, 0), (1, 0)),
            ('SPAN', (0, 1), (1, 1)),
            ('SPAN', (0, 2), (1, 2)),
            ('SPAN', (0, 3), (1, 3)),
            ('SPAN', (2, 2), (-1, 2)),# row 2
            ('SPAN', (0, 3), (-1, 3)),# row 3
            ('ALIGN', (0, 4), (-1, 4), 'CENTER'),
            ## Header row bottom padding
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Gridlines
                ])
            
            body_style = TableStyle([
            ('WORDWRAP', (0, 4), (-1, 4)),
            ('WORDWRAP', (0, 12), (-1, -1)),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            
            
            #('SPAN', (1, 5), (2, 5)),# row 4 
            ('SPAN', (0, 4), (3, 4)),# row 4 
            ('SPAN', (1, 5), (3, 5)),# row 5
            ('SPAN', (1, 6), (3, 6)),# row 6
            ('SPAN', (1, 7), (3, 7)),# row 7
            ('SPAN', (1, 8), (3, 8)),
            ('SPAN', (1, 9), (3, 9)),
            ('SPAN', (1, 10), (3, 10)),
            ('SPAN', (1, 11), (3,11)),
            ('FONTNAME', (0, 12), (-1, 12), 'Helvetica-Bold'),  
            ('ALIGN', (0, 12), (5, 12),'RIGHT'),
            ('SPAN', (0, 12), (5, 12)),
            ('SPAN', (0, 13), (3, 13)),
            ('SPAN', (0, 14), (3, 14)),
            ('SPAN', (0, 15), (3, 15)),
            ('SPAN', (0, 16), (-1, 16)),
            ('SPAN', (0, 17), (1, 18)),
            ('VALIGN', (0, 17), (1, 18), 'MIDDLE'),
            ('ALIGN', (0, 17), (-1, -1),'CENTER'),
            ('SPAN', (3, 17), (4, 17)),
            ('SPAN', (5, 17), (6, 17)),
            ('SPAN', (0, 18), (1, 18)),
            ('SPAN', (3, 18), (4, 18)),
            ('SPAN', (5, 18), (6, 18)),
            ('SPAN', (0, 19), (1, 19)),
             ('SPAN', (3, 19), (4, 19)),
            ('SPAN', (5, 19), (6, 19)),
           
            ])
            
             # Create a table and apply styles
            table.setStyle(style)
            table.setStyle(body_style)
            #table.setStyle(signature_style)
            elements.append(table)
            table.wrapOn(pdf, 0, 0)
            table.drawOn(pdf, 50, 200)
            pdf.rect(50, 50, width=500, height=150)
            pdf.drawString(230, 100, "For Accounts Dept Use only")
            pdf.save()
            pdf_data = buffer.getvalue()
            buffer.close()  
            return pdf_data
           

@login_required    
def Travelclaimrequest(request):
    try:
        user = request.user  
        print(request.user)
        if request.method == 'POST':
            form = TravelclaimForm(request.POST,request.FILES)
            email = 'ajmalummer30@gmail.com'        
            if form.is_valid():
                instance =form.save(commit=False)
                instance.user =request.user
                instance.Total_Amount = int(instance.accommodation) + int(instance.meals)+ int(instance.transportation)+ int(instance.miscellaneous)
                instance.save()
                pdf_data=travelclaimpdf(instance)
                user_info = str(request.user)
                claimant = instance.user.first_name+' '+instance.user.last_name
                claim_id =instance.id
                form_no=str(claim_id)   
                token = TimestampSigner().sign(claim_id)
                #expiry_time = timezone.now() + datetime.timedelta(hours=24)
                approve_url = request.build_absolute_uri(reverse('pettycash:handle_approval', args=[claim_id, 'approve'])) + '?token=' + token
                message = render_to_string('travelclaim/tc_Template_Manageremail.html', {'instance': instance,'token': token,'approve_url': approve_url})
                Manageremail = EmailMessage(
                    subject='Approval Request-Travel Claim- Employee Name -'+ user_info+' - Employee ID -'+claimant+' -Request No:'+form_no,
                    body=message,
                    from_email='ajmal.ummer@sats.com.sa',
                    to=[email]  
                    )
                Manageremail.attach('report.pdf', pdf_data, 'application/pdf')
                Manageremail.content_subtype = 'html'
                Manageremail.send()
                context = {
                        'instance':instance
                        }
                messages.success(request, "Request submitted successfully.")
                return redirect('pettycash:ViewUserTravelClaims')
                #return render(request, 'travelclaim/tc_download_pdf.html', context)  
            else:
                print(form.errors) 
                user = request.user
                form = TravelclaimForm(request.POST,request.FILES)
                forminfo=travelclaiminfo(user)
                context ={
                    'form':form,
                    'forminfo':forminfo     
                    }
               
                return render(request,'travelclaim/tc_create.html',context)
                
        else:  
            user = request.user
            if not hasattr(user, 'manager'):
                raise Exception("User's manager is missing.")
            if not hasattr(user.manager, 'email'):
                raise Exception("User's manager value is missing.")
            form = TravelclaimForm()
            forminfo=travelclaiminfo(user)
            context ={
                'form':form,
                'forminfo':forminfo     
            }
            return render(request,'travelclaim/tc_create.html',context)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'travelclaim/error_template.html', {'error_message': error_message})

def travelclaimpdfdownload(request,id):
    if request.method=='POST':
        print('post')       
    else:
        instance= TravelClaim.objects.get(id=id)
        print(instance)
        pdf_data=travelclaimpdf(instance)   
        response = HttpResponse(pdf_data, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        return response
    
def pettycashpdfdownload(request,id):
    if request.method=='POST':
        print('post')      
    else:
        pdf_data = pdfgenerate(id)   
        response = HttpResponse(pdf_data, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Petty Cash Form.pdf"'
        return response

def handle_approval(request ,claim_id,action):
    try:
        token = request.GET.get('token')
        claim_id = TimestampSigner().unsign(token, max_age=300)  # 24 hours in seconds
    except (SignatureExpired, BadSignature):
        return HttpResponse("Invalid or expired link.")
        
    if action == 'Approve':
        claim = TravelClaim.objects.get(pk=claim_id)
        claim.status = True
        claim.approved_date= timezone.now()
        claim.save()
        return HttpResponse("Claim approved successfully")
    else:
        return HttpResponse("Claim rejected successfully")
    

class ProductInline():
    form_class = ExpenseForm
    model = Expense
    template_name = "pettycash/product_create_or_update.html"
    
    
    def get_initial(self):    
            initial = super().get_initial()
            initial['claimant'] = f"{self.request.user.first_name} {self.request.user.last_name}"
            initial['Manager_Email'] = self.request.user.manager.email     
            # Add more initial values for other fields if needed
            return initial
      
    def form_valid(self, form):
        form.instance.employee = self.request.user
        form.instance.station_name=self.request.user.station_name
        Manager_email=self.request.user.manager.email
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))
        self.object = form.save()
        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        total_amount = ExpenseItem.objects.filter(expense=self.object).aggregate(Sum('amount'))['amount__sum']
        
        self.object.total_amount = total_amount if total_amount else 0
        self.object.save()
        last_instance = Expense.objects.latest('id')
        pdf_data = pdfgenerate(last_instance.id)
        user_info = last_instance.employee.employee_id
        claimant = last_instance.employee.first_name+' '+last_instance.employee.last_name
        claim_id =last_instance.id
        
        token = TimestampSigner().sign(last_instance.id)
        
        message = render_to_string('pettycash/pc_Template_Manageremail.html', {'instance': last_instance,'token': token,})
        Manageremail = EmailMessage(
                subject='Approval Request-PettyCash- Employee Name -'+ claimant+' - Employee ID -'+user_info+' -Request No:'+str(claim_id),
                body=message,
                from_email='ajmal.ummer@sats.com.sa',
                to=[Manager_email]  
                )
        Manageremail.attach('Pettycashform.pdf', pdf_data, 'application/pdf')
        Manageremail.content_subtype = 'html'
       # Manageremail.send()  
        messages.success(self.request, "Your request has been submitted successfully.")
        return redirect('pettycash:ViewUserPettyCash')
        """ response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Petty Cash Form.pdf"'
        response.write(pdf_data)
        return response """
        

    def formset_variants_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  
        #self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        #set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.expense = self.object
            variant.amount = variant.quantity*variant.unit_price
            variant.save()
            
@method_decorator(login_required, name='dispatch')
class ProductCreate(ProductInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': ExpenseItemFormSet(prefix='variants'),
                
            }
        else:
            return {
                'variants': ExpenseItemFormSet(self.request.POST or None, prefix='variants'),
                
            }

class ProductUpdate(ProductInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': ExpenseItemFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            
        }

class ProductList(ListView):
    model = Expense
    template_name = "pettycash/product_list.html"
    context_object_name = "products"
    
@login_required    
def displayclaims(request):
    
     if request.method == 'GET':
        form=ExpenseForm()
        start_date = request.GET.get('Start_date')
        end_date = request.GET.get('End_date')
        station_name = request.GET.get('station_name')
        form_id = request.GET.get('form_id')
         
        # Assuming 'start_date' and 'End_date' are in 'YYYY-MM-DD' format
        if start_date and end_date and station_name:
            claims = Expense.objects.filter(
                date__range=[start_date, end_date],station_name=station_name
            )
            if not claims:
                if station_name == 3:
                    station_name="JED"
                elif station_name ==2 :
                    station_name= "RUH"
                else:
                    station_name="DMM"
                
                messages.success(request, 'No data found between '+ start_date + ' and ' + end_date +' for '+ station_name +' Station' )
                return render(request, 'pettycash/product_list.html')
            else:
                print(claims)
                return render(request, 'pettycash/product_list.html', {'products': claims,'form':form})
            
        elif start_date and end_date :
            claims = Expense.objects.filter(
                date__range=[start_date, end_date]
            )
            if not claims:
                
                messages.success(request, 'No data found between'+ start_date + 'and' + end_date)
                return render(request, 'pettycash/product_list.html')

                
            else:
                
                return render(request, 'pettycash/product_list.html', {'products': claims,'form':form})
        elif form_id:
            claims = Expense.objects.filter(id=form_id)
            if not claims:
                
                messages.success(request, 'No data found for the supplied ID '+ form_id)
                return render(request, 'travelclaim/product_list.html')
            else:
                return render(request, 'pettycash/product_list.html', {'products': claims,'form':form})
                       
        else:
           
            claims = Expense.objects.all().order_by('-date')
            return render(request, 'pettycash/product_list.html', {'products': claims,'form':form})
    
def delete_variant(request, pk):
    try:
        variant = ExpenseItem.objects.get(id=pk)
    except ExpenseItem.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('pettycash:update_product', pk=variant.expense.id)

    variant.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('pettycash:update_product', pk=variant.expense.id)

@login_required
def ViewUserTravelClaims(request):
    try:
        if request.method=='POST':
            print("post")
        else:
            
            user = request.user
            claims = TravelClaim.objects.filter(user=user).order_by('-created_date')
            if not claims:
                    messages.error(request, 'You dont have any requests to show',extra_tags='info')
            return render(request, 'travelclaim/mytravelclaimview.html', {'claims': claims})
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'travelclaim/error_template.html', {'error_message': error_message})

@login_required
def ViewUserPettyCash(request):
    try:
        if request.method=="POST":
            print("post")
        else: 
            user = request.user
            pettycash_obj = Expense.objects.filter(employee=user).order_by('-id')
            total_sum = pettycash_obj.aggregate(total_sum=Sum('total_amount'))['total_sum']
            if not pettycash_obj:
                messages.error(request, 'You dont have any requests to show',extra_tags='info')
            return render(request, 'pettycash/mypettycashview.html', {'products': pettycash_obj, 'total_sum': total_sum})
   
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'travelclaim/error_template.html', {'error_message': error_message})
    
@login_required
@group_required(['Finance']) 
def ViewAllUserPettyCash(request):
    try:
        if request.method=="POST":
            print("post")
        else: 
            form=ExpenseFilterForm()
            pettycash_obj = Expense.objects.all().order_by('-id')
            total_sum = pettycash_obj.aggregate(total_sum=Sum('total_amount'))['total_sum']

            if not pettycash_obj:
                messages.error(request, 'You dont have any requests to show',extra_tags='info')
            return render(request, 'pettycash/AllUserpettycashview.html', {'products': pettycash_obj,'total_sum': total_sum,'form':form })
   
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'travelclaim/error_template.html', {'error_message': error_message})

def ViewUserPettyCashDetail(request,id):
    if request.method=="POST":
        print("post")
    else: 
        user = request.user
        pettycash_obj = Expense.objects.get(id=id)
        expense_obj=ExpenseItem.objects.filter(expense=pettycash_obj)
        #return render(request, 'travelclaim/mytravelclaimview.html', {'claims': pettycash_obj})
        return render(request, 'pettycash/pc_Detailview.html', {'invoice_items': pettycash_obj, 'line_items':expense_obj })
    
def MgrEmailclaimView(request,id):
    if request.method =='POST':
        print('post')
    else:
        instance_obj= TravelClaim.objects.get(id=id)
        return render(request,'travelclaim/tc_mgr_emailapprove.html',{'instance':instance_obj})
    


def ApproveTravelClaim(request,id,action):
    try:    
        if action == 'Approve':
            instance = TravelClaim.objects.get(pk=id)
            if instance.status == True:
                return HttpResponse('Claim already approved')
            elif instance.user.manager != request.user:
                return HttpResponse('not authorised to approve the claim')
            else: 

                instance.status = True
                instance.approved_date= timezone.now()
                instance.save()
                claimant = instance.user.first_name+' '+instance.user.last_name
                form_no =str(instance.id)
                user_info = str(request.user)
                useremail= instance.user.email
                message = render_to_string('travelclaim/tc_Template_UserPostApprove.html', {'instance': instance})
                UserEmail = EmailMessage(
                        subject=' TravelClaim Approved - Employee Name -'+ user_info+' - Employee ID -'+claimant+' -Request No:'+form_no,
                        body=message,
                        from_email='ajmal.ummer@sats.com.sa',
                        #to=[useremail]  
                        to=['ajmalummer30@gmail.com'] 
                        )
                UserEmail.content_subtype = 'html'
                #UserEmail.send()
                messages.success(request, "Claim Approved successfully.")
                return redirect('pettycash:Tc_Manager_View')
    except TravelClaim.DoesNotExist:
        return HttpResponse("TravelClaim with provided ID does not exist")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")
    

def ApprovePettyCash(request,id,action):
    try:    
        if action == 'Approve':
            instance = Expense.objects.get(pk=id)
            if instance.Approved_status == True:
                return HttpResponse('Claim already approved')
            elif instance.employee.manager != request.user:
                return HttpResponse('not authorised to approve the claim')
            else: 

                instance.Approved_status = True
                instance.approved_date= timezone.now()
                instance.save()
                claimant = instance.employee.first_name+' '+instance.employee.last_name
                form_no =str(instance.id)
                user_info = str(instance.employee.employee_id)
                useremail= instance.employee.email
                message = render_to_string('pettycash/pc_Template_UserPostApprove.html', {'instance': instance})
                UserEmail = EmailMessage(
                        subject=' PettyCash Approved - Employee Name -'+claimant+' - Employee ID -'+user_info+' -Request No:'+form_no,
                        body=message,
                        from_email='ajmal.ummer@sats.com.sa',
                        #to=[useremail]  
                        to=['ajmalummer30@gmail.com'] 
                        )
                UserEmail.content_subtype = 'html'
                #UserEmail.send()
                messages.success(request, "PettyCash Approved successfully.")
                return redirect('pettycash:Pc_Manager_View')
    except TravelClaim.DoesNotExist:
        return HttpResponse("TravelClaim with provided ID does not exist")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")

        
@login_required 
@group_required(['Manager'])  
def Tc_Manager_View(request):
    try:
        manager_claims_pending = TravelClaim.objects.filter(user__manager=request.user, status=False).order_by('-created_date')
        manager_claims_approved = TravelClaim.objects.filter(user__manager=request.user, status=True).order_by('-id')
       
        if not manager_claims_pending and not manager_claims_approved :
            messages.success(request, 'You dont have any requests to show')
            
        # Pass the two querysets to the template for rendering
        return render(request, 'travelclaim/TcManageview.html', {'pending_claims': manager_claims_pending, 'approved_claims': manager_claims_approved})
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'travelclaim/error_template.html', {'error_message': error_message})
    
      
@login_required 
@group_required(['Manager'])  
def Pc_Manager_View(request):
    try:
        manager_claims_pending = Expense.objects.filter(employee__manager=request.user, Approved_status=False).order_by('-date')
        manager_claims_approved = Expense.objects.filter(employee__manager=request.user, Approved_status=True).order_by('-id')
        if not manager_claims_pending and not manager_claims_approved :
            messages.success(request, 'You dont have any requests to show')
            
        # Pass the two querysets to the template for rendering
        return render(request, 'pettycash/PcManageview.html', {'pending_claims': manager_claims_pending, 'approved_claims': manager_claims_approved})
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'travelclaim/error_template.html', {'error_message': error_message})

def filter_petty_requests(request):

    form=ExpenseFilterForm()
    filters = {}
    for key, value in request.GET.items():
        if value:
            filters[key] = value

    start_date_str = filters.get('Start_date')
    end_date_str = filters.get('End_date')
    station_name = filters.get('station_name') 
    employee = filters.get('employee') 

    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None
    except ValueError:
    # Handle invalid date format
        start_date = None
        end_date = None

    query_filters = Q()
    if start_date:
        query_filters &= Q(date__gte=start_date)
    if end_date:
        query_filters &= Q(date__lte=end_date)
    if station_name:
        query_filters &= Q(station_name=station_name)
    if employee:
        query_filters &= Q(employee=employee)

        print(query_filters)

    petty_requests = Expense.objects.filter(query_filters)
    total_sum = petty_requests.aggregate(total_sum=Sum('total_amount'))['total_sum']

    if not petty_requests:
        messages.error(request, 'You dont have any requests to show',extra_tags='info')
    return render(request, 'pettycash/AllUserpettycashview.html', {'products': petty_requests,'total_sum': total_sum,'form':form })