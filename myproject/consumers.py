import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import pytz
from myproject.tasks import generate_speech, test_file_creation
from websockets.models import  Ticket
from datetime import datetime, timedelta
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch,mm
from django.contrib.staticfiles import finders
import cups
from django.conf import settings
import os
from django.utils import timezone
import io
import tempfile
import subprocess
from django.core.exceptions import ObjectDoesNotExist
import pyttsx3
import io
import tempfile
import subprocess





class QueueConsumer(WebsocketConsumer):

    
    
    max_ticket_number = 8  
    last_ticket_date = None 
    

    current_queue_number = None  # Store the current queue number
    current_counter = None


    @staticmethod
    def create_ticket_pdf(ticket_number, date, logo_path,output_path):
        buffer = io.BytesIO()
        #c = canvas.Canvas(buffer, pagesize=(80 * mm, 55* mm))
        c = canvas.Canvas(output_path, pagesize=(80 * mm, 55 * mm))
        
        # Logo setup
        logo_width, logo_height = 40 * mm, 10 * mm
        logo_x = (80 * mm - logo_width) / 2
        logo_y = 45 * mm

        c.drawImage(logo_path, x=logo_x, y=logo_y, width=logo_width, height=logo_height)

        c.setFont("Helvetica-Bold", 12)

        formatted_date = date.strftime('%d-%m-%Y')
        formatted_time = date.strftime('%H:%M:%S')
        token_number_str = "Token Number: " + str(ticket_number)
        token_number_width = c.stringWidth(token_number_str, "Helvetica-Bold", 12)
        c.drawString((80 * mm - token_number_width) / 2, 35 * mm, token_number_str)
        
        c.rect((80 * mm - 50 * mm) / 2, 30 * mm, 50 * mm, 10 * mm, stroke=1, fill=0)
        
        c.setFont("Helvetica", 10)
        date_str = f"Date: {formatted_date}"
        time_str = f"Time: {formatted_time}"
        date_width = c.stringWidth(date_str, "Helvetica", 10)
        time_width = c.stringWidth(time_str, "Helvetica", 10)
        c.drawString((80 * mm - date_width) / 2, 20 * mm, date_str)
        c.drawString((80 * mm - time_width) / 2, 10 * mm, time_str)
            
        
        #c.showPage()
        c.save()
        #buffer.seek(0)

        #return buffer

    @staticmethod
    def print_to_printer(pdf_buffer):
        conn = cups.Connection()
        printers = conn.getPrinters()
        print("Available printers:")
        for printer in printers:
            print(printer)

        preferred_printer = "EPSON_TM-T20III"
        #preferred_printer = "Generic-POS-Printer"

        if preferred_printer in printers:
            printer_name = preferred_printer
        elif not preferred_printer:
            printer_name = list(printers.keys())[0] 
        else:
            raise ValueError(f"Preferred printer '{preferred_printer}' not found. Available printers: {', '.join(printers.keys())}")

        # Define the custom media size
        options = {
         "media": "Custom.226x144",
         "orientation-requested": "4",
         "fit-to-page": "true",
        }
        if isinstance(pdf_buffer, io.BytesIO):
        # Write buffer to a temporary file
            temp_pdf_path = tempfile.mktemp(suffix=".pdf")
            with open(temp_pdf_path, 'wb') as temp_pdf_file:
                temp_pdf_file.write(pdf_buffer.getvalue())

        # Print the PDF file using the temporary file path
            print_job_id = conn.printFile(printer_name, temp_pdf_path, "Print Job", options)

           

        # Clean up the temporary file
            os.remove(temp_pdf_path)
        else:
        # Assume pdf_buffer is a path to the file
            print_job_id = conn.printFile(printer_name, pdf_buffer, "Print Job", options)

        return print_job_id

        
    def connect(self):
        self.group_name = 'queue_group'

       

        # Join group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')
        mobile_number = text_data_json.get('phone_number')
       
       
        if action == 'issue_ticket':

            current_system_date = datetime.now().date() 
            str_current_system_date= str(current_system_date)
        
            try:
                last_ticket = Ticket.objects.latest('id')
                last_ticket_number = last_ticket.ticket_number
                
                
                local_tz = pytz.timezone('Asia/Riyadh')  # Replace with your desired time zone
                issued_at_local = last_ticket.issued_at.astimezone(local_tz)
                formatted_issued_at = issued_at_local.strftime('%Y-%m-%d')
            except Ticket.DoesNotExist:
                last_ticket_number = 0 
                formatted_issued_at = str_current_system_date
                
            
            
            if str_current_system_date > formatted_issued_at :
                last_ticket_number = 0
                
                
            new_ticket_number = last_ticket_number + 1

            ticket_obj = Ticket.objects.create(ticket_number=new_ticket_number)
            ticket_obj.mobile_number=mobile_number
            ticket_obj.save()
            uncalled_ticket_count = Ticket.objects.filter(called=False).count()
            last_called_obj=None
            
            try:
                # Attempt to retrieve the latest 'called' Ticket object
                last_called_obj = Ticket.objects.filter(called=True).latest('id')
                last_called_obj_ticket=last_called_obj.ticket_number
            except ObjectDoesNotExist:
                # Handle the case where no such object exists
                last_called_obj_ticket = 0

            local_tz = pytz.timezone('Asia/Riyadh')  # Replace with your desired time zone
            issued_at_local = ticket_obj.issued_at.astimezone(local_tz)
            formatted_issued_at = issued_at_local.strftime('%d-%m-%Y %H:%M:%S')

            logo_path = finders.find('satsksa.png')
            if not logo_path:
                raise FileNotFoundError("Logo image not found.")
            
            
            # Broadcast the new ticket number to the group
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'ticket_issued',
                    'id' : ticket_obj.id,
                    'ticket_number': ticket_obj.ticket_number,
                    'issued_at': formatted_issued_at,
                     'uncalled_ticket_count':uncalled_ticket_count,
                     'last_called_obj':last_called_obj_ticket,
                     'mobile_number':ticket_obj.mobile_number,
                    

                }
            )
            

        elif action == 'call_queue':
            queue_number = text_data_json['queue_number']
            counter = text_data_json['counter']
            uncalled_ticket_count = Ticket.objects.filter(called=False).count()
            last_created_obj_ticket_number = 0
            try:
                last_created_obj= Ticket.objects.filter(called=False).latest('id')
                last_created_obj_ticket_number=last_created_obj.ticket_number
            except Ticket.DoesNotExist:
                last_created_obj_ticket_number=0

            
            text = f" Token No {queue_number} counter No {counter}"
            res=generate_speech.delay(text)
            try:
                res_value = res.get(timeout=10)
                print(f"Result audio: {res_value}")
            except Exception as e:
                    res_value = None
                    print(f"An error occurred: {e}")
                    
                        
            
                    
            
            # Broadcast the queue number to the group
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'queue_update_manual',
                    'queue_number': queue_number,
                    'counter': counter,
                    'uncalled_ticket_count':uncalled_ticket_count,
                    'last_created_obj':last_created_obj_ticket_number,
                    'audio_url': res_value
                    
                }
            )

           
            
        elif action == 'call_queue_db':
            counter = text_data_json['counter']
    
            try:
                next_ticket = Ticket.objects.filter(called=False).order_by('issued_at').first()
                last_created_obj = Ticket.objects.latest('id')
                last_created_obj_ticket_number=last_created_obj.ticket_number
                last_called_obj = Ticket.objects.filter(called=True).order_by('issued_at').last()
                last_called_ticket_number = last_called_obj.ticket_number if last_called_obj else None
            except Ticket.DoesNotExist:
                next_ticket =None
                last_created_obj_ticket_number =0
                last_called_ticket_number=None


            
            if next_ticket:
                    next_ticket.called = True
                    next_ticket.counter_number=counter
                    next_ticket.save()

                    local_tz = pytz.timezone('Asia/Riyadh')  # Replace with your desired time zone
                    issued_at_local = next_ticket.issued_at.astimezone(local_tz)
                    formatted_issued_at = issued_at_local.strftime('%d-%m-%Y %H:%M:%S')
                    issued_at =formatted_issued_at if last_called_obj else None
                
                    uncalled_ticket_count = Ticket.objects.filter(called=False).count()
                    QueueConsumer.current_queue_number = next_ticket.ticket_number
                    QueueConsumer.current_counter = counter

                    # Log for debugging
                    print(f"Calling ticket: {next_ticket.ticket_number} for counter {counter}")
                    text = f" Token {next_ticket.ticket_number} counter {counter}"
            
                    res=generate_speech.delay(text)
                    try:
                        res_value = res.get(timeout=10)
                        print(f"Result: {res_value}")
                    except Exception as e:
                      res_value = None
                      print(f"An error occurred: {e}")
 
                    """  result = test_file_creation.delay(text)
                    try:
                        result_value = result.get(timeout=10)
                        print(f"Result: {result_value}")
                    except Exception as e:
                        print(f"An error occurred: {e}") """

                    
                    #

                    # Broadcast the queue number to the group
                    async_to_sync(self.channel_layer.group_send)(
                        self.group_name,
                        {
                            'type': 'queue_update',
                            'queue_number': next_ticket.ticket_number,
                            'counter': counter,
                            'uncalled_ticket_count': uncalled_ticket_count,
                            'last_created_obj': last_created_obj_ticket_number,
                            'id' : next_ticket.id,
                            'audio_url': res_value
                        }
                    )

                    self.send(text_data=json.dumps({
                    'type': 'queue_specific_update',
                    'counter': counter,
                    'queue_number': next_ticket.ticket_number,
                    'mobile_number': next_ticket.mobile_number,
                    'issued_at': issued_at,
                    'id' :next_ticket.id
                
                   
                }))
            else:
                    # If there is no next_ticket, handle it here
                async_to_sync(self.channel_layer.group_send)(
                        self.group_name,
                        {
                            'type': 'queue_empty',
                            'counter': counter,
                            'last_created_obj': last_created_obj_ticket_number,
                            'last_called_obj':  last_called_ticket_number,
                            

                        }
                    )

                

           
                



           

        elif action == 'recall-queue_db':
            counter = text_data_json['counter']
            uncalled_ticket_count = Ticket.objects.filter(called=False).count()

            if uncalled_ticket_count == 0 :
                last_called_obj = Ticket.objects.filter(called=True).order_by('issued_at').last()
                last_called_ticket_number = last_called_obj.ticket_number if last_called_obj else None

                
                try:
                
                    last_created_obj= Ticket.objects.latest('id')
                    last_created_obj_ticket_number = last_created_obj.ticket_number
                except Ticket.DoesNotExist:
                    last_created_obj_ticket_number = 0


                async_to_sync(self.channel_layer.group_send)(
                        self.group_name,
                        {
                            'type': 'queue_empty',
                            'counter': counter,
                            'last_created_obj': last_created_obj_ticket_number,
                            'last_called_obj':  last_called_ticket_number

                        }
                    )


            else: 

                last_called_obj = Ticket.objects.filter(called=True,counter_number=counter).last()
                last_called_ticket_number = last_called_obj.ticket_number if last_called_obj else None
                try:
                
                    last_created_obj= Ticket.objects.latest('id')
                    last_created_obj_ticket_number = last_created_obj.ticket_number
                except Ticket.DoesNotExist:
                    last_created_obj_ticket_number = 0

                if not last_called_obj :
                     self.send(text_data=json.dumps({
                            'type': 'forget_queue_call',
                            'counter': counter,
                            'last_created_obj': last_created_obj_ticket_number,
                            'last_called_obj':  last_called_ticket_number
                
                   
                        }))



                    

                else:


                    local_tz = pytz.timezone('Asia/Riyadh')  # Replace with your desired time zone
                    issued_at_local = last_called_obj.issued_at.astimezone(local_tz)
                    formatted_issued_at = issued_at_local.strftime('%d-%m-%Y %H:%M:%S')
                    issued_at =formatted_issued_at if last_called_obj else None

                    QueueConsumer.current_queue_number=last_called_ticket_number
                    mobile_number =last_called_obj.mobile_number if last_called_obj else None


            
                    try:
                    
                        last_created_obj= Ticket.objects.latest('id')
                        last_created_obj_ticket_number = last_created_obj.ticket_number
                    
                    except Ticket.DoesNotExist:
                        last_created_obj_ticket_number = 0
                    # Broadcast the queue number to the group
                    async_to_sync(self.channel_layer.group_send)(
                        self.group_name,
                        {
                            'type': 'queue_update',
                            'queue_number': QueueConsumer.current_queue_number,
                            'counter': counter,
                            'uncalled_ticket_count':uncalled_ticket_count,
                            'last_created_obj':last_created_obj_ticket_number,
                            'id' : last_called_obj.id,
                            
                        
                        }
                    )
                    self.send(text_data=json.dumps({
                        'type': 'queue_specific_update',
                        'counter': counter,
                        'queue_number': QueueConsumer.current_queue_number,
                        'mobile_number': mobile_number,
                        'issued_at': issued_at
                    }))

        elif action == 'move_back':
            
            if QueueConsumer.current_queue_number:

                # Log for debugging
                print(f"Moving ticket: {QueueConsumer.current_queue_number} back to queue from counter {QueueConsumer.current_counter}")
            else:
                 print(f"empty {QueueConsumer.current_queue_number} ")


            
        elif text_data_json.get('type') == 'ping':
            # Broadcast pong to the group
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'pong'
                }
            )

        
    def ticket_issued(self, event):
        ticket_number = event['ticket_number']
        issued_at = event['issued_at']
        uncalled_ticket_count =event['uncalled_ticket_count']
        last_called_obj =event['last_called_obj']
        id = event['id']
        mobile_number = event['mobile_number']
        
       
      
        # Send the new ticket number to WebSocket
        self.send(text_data=json.dumps({
            'type': 'ticket_issued',
            'ticket_number': ticket_number,
            'issued_at': issued_at,
            'uncalled_ticket_count':uncalled_ticket_count,
            'last_called_obj':last_called_obj,
            'mobile_number':mobile_number,
            'id' : id,
            
            
        }))

    def queue_update_manual(self, event):
        queue_number = event['queue_number']
        counter = event['counter']
        uncalled_ticket_count =event['uncalled_ticket_count']
        last_created_obj =event['last_created_obj']
        audio_url = event['audio_url']

        self.send(text_data=json.dumps({
            'type': 'queue_update_manual',
            'queue_number': queue_number,
            'counter': counter,
            'uncalled_ticket_count':uncalled_ticket_count,
            'last_created_obj':last_created_obj,
            'audio_url': audio_url

        }))

    def queue_update(self, event):
        queue_number = event['queue_number']
        counter = event['counter']
        uncalled_ticket_count =event['uncalled_ticket_count']
        last_created_obj =event['last_created_obj']
        id = event['id']
        audio_url = event['audio_url']

        # Send the queue number to WebSocket
        self.send(text_data=json.dumps({
            'type': 'queue_update',
            'queue_number': queue_number,
            'counter': counter,
            'uncalled_ticket_count':uncalled_ticket_count,
             'last_created_obj':last_created_obj,
              'id' : id,
              'audio_url': audio_url
              
            
        }))

    def queue_empty(self,event):
        counter = event['counter']
        last_created_obj = event['last_created_obj']
        last_called_obj = event['last_called_obj']
       

        self.send(text_data=json.dumps({
            'type': 'queue_empty',
            'counter': counter,
            'last_created_obj': last_created_obj,
            'last_called_obj':  last_called_obj
           
        }))


    def pong(self, event):
        # Send pong response to WebSocket
        self.send(text_data=json.dumps({
            'type': 'pong'
        }))

