import logging
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from gtts import gTTS
import os

import redis
from myproject.tasks import add, generate_speech
from websockets.models import  Ticket
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import pyttsx3
import io
import tempfile
from celery.exceptions import OperationalError
import logging
from celery.exceptions import TimeoutError

# Configure the logger
logger = logging.getLogger(__name__)  # It's good practice to use __name__ to make the logger's output more understandable.
logger.setLevel(logging.ERROR)  


@login_required
def staff_view(request):
    if request.method=='POST':
        print('POST')
    else:
        user = request.user 
        if user.is_authenticated:

            try:
                counter = user.Web_profile.counter.id
                open_tickets_obj=Ticket.objects.filter(called=False)
                last_called_obj_counter_specific = Ticket.objects.filter(called=True,counter_number=counter).order_by('issued_at').last()
                last_called_obj = Ticket.objects.filter(called=True).order_by('issued_at').last()
                last_issued_ticket=Ticket.objects.latest('id')
                count=open_tickets_obj.count()
            except ObjectDoesNotExist:
                open_tickets_obj=None
                last_called_obj_counter_specific = None
                last_issued_ticket=None
                last_called_obj=None
                count=0

        
        context={
                    'open_ticket' : open_tickets_obj,
                     'current_ticket' :last_called_obj_counter_specific,
                     'last_issued_ticket' :last_issued_ticket,
                     'open_tickets_count' :count,
                     'last_called_obj': last_called_obj,
        }
    
        try:
            result = add.delay(10, 20)
            print(f"Task ID: {result.id}")

            # Check the state of the task
            print(f"Task State: {result.state}")  # Possible values include PENDING, SUCCESS, FAILURE, etc.

            # Get the result of the task (this will block until the task is done)
            result_value = result.get(timeout=10)  # Waits for 10 seconds for the task to complete
            print(f"Task Result: {result_value}")
        except OperationalError as e:
            logger.error("Failed to connect to Celery broker: %s", e)
        except AttributeError as e:
            logger.error("AttributeError in Celery task: %s", e)
        
        #generate_speech('Ajmal Ummer is an idiot.she is traitor and used to fight with me and abuise me')
        return render(request, 'websockets/staff.html',context)

def display_view(request):
    
    return render(request, 'websockets/display.html')


def issue_queue_view(request):


    return render(request, 'websockets/issue_queue.html')

# New view for end users to issue tickets
def issue_ticket_view(request):
   
    return render(request, 'websockets/issue_ticket.html')


def generate_announcement(request, token_number, counter_number):
    announcement_text = f"Token number {token_number}, please proceed to counter number {counter_number}."
    tts = gTTS(text=announcement_text, lang='en')
    audio_file_path = f"static/sound/announcement_{token_number}_{counter_number}.mp3"
    tts.save(audio_file_path)
    return HttpResponse(content_type="application/json", status=200)


def get_last_ticket_number(request):
    try:
        last_ticket = Ticket.objects.latest('id')  # Assuming 'id' is your primary key
        ticket_number = last_ticket.ticket_number
    except Ticket.DoesNotExist:
        ticket_number = 0
    return JsonResponse({'ticket_number': ticket_number})

def get_open_tickets(request):
    if request.method=='POST':
        print('POST')
    else:
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)

        # Get tomorrow's date as a datetime object at midnight in UTC
        tomorrow_start = today_start + timezone.timedelta(days=1)

       

        """  open_tickets_count = Ticket.objects.filter(
            called=False, 
            issued_at__gte=today_start, 
            issued_at__lt=tomorrow_start
        ).count()"""

        open_tickets_obj=Ticket.objects.filter(called=False)
        return render(request, 'websockets/staff.html',{'open_ticket' : open_tickets_obj})
       

def text_to_speech(request):
    # Get the text from the request
    #text = request.GET.get('text', 'Hello, welcome to our website!')
    text =   'Hello, welcome to our website!'

    # Initialize pyttsx3 engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 3)
   

    # Generate a unique filename for each audio file
    filename = "speech_{}.mp3".format(os.getpid())
    filepath = os.path.join(settings.MEDIA_ROOT, 'queu',filename)

    # Save speech to a file in the media directory
    engine.save_to_file(text, filepath)
    engine.runAndWait()

    # Ensure the engine has finished processing
    engine.stop()

    # Open and read the file
    with open(filepath, 'rb') as f:
        audio_data = f.read()

    if os.path.exists(filepath):
        print(f"File {filepath} exists, size: {os.path.getsize(filepath)} bytes")
    else:
        print(f"File {filepath} does not exist")

    full_path = os.path.abspath(filepath)
    print("Full path to file:", full_path)
    # Optionally, clean up the file if you don't want to store it
    #os.remove(filepath)

    # Generate a response
    response = HttpResponse(audio_data, content_type='audio/mpeg')
    response['Content-Disposition'] = 'inline; filename="{}"'.format(filename)
    return response
