import os
from celery import shared_task
from django.conf import settings
import logging
import uuid
from datetime import datetime
from django.http import HttpResponse
from pydub import AudioSegment
from gtts import gTTS
from django.core.mail import send_mail
from django.utils.timezone import now, localtime
from datetime import timedelta
from django.utils import timezone
from django.db.models import Max
from django.db.models import Max, OuterRef, Subquery


from polls.models import Fa_Contract, PreventiveMaintenance

logger = logging.getLogger(__name__)

@shared_task
def generate_speech(text):
    print('ajmal')
    try:
        print("Starting generate_speech task")
        print(f"Received text: {text}")

        # Generate a unique filename for each audio file
        unique_id = uuid.uuid4()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"speech_{timestamp}_{unique_id}.mp3"
        directory = os.path.join(settings.MEDIA_ROOT, 'queu')
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        
        filepath = os.path.join(directory, filename)
        print(f"Filepath for speech: {filepath}")

        # Generate speech using gTTS and save to file
        tts = gTTS(text=text, lang='en')
        tts.save(filepath)
        print("Speech saved to file")


        # Check if the file exists and log its size
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            print(f"File {filepath} exists, size: {file_size} bytes")
        else:
            logger.error(f"File {filepath} does not exist")

        # Full path to the file
        full_path = os.path.join(settings.MEDIA_URL, 'queu', filename)
        print(f"Full path to file: {full_path}")
        return full_path

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

@shared_task
def add(x, y):
    return x + y



@shared_task
def test_file_creation(text):
    try:
        #filename = "test_{}.txt".format(os.getpid())
        unique_id = uuid.uuid4()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"speech_{timestamp}_{unique_id}.txt"
        directory = os.path.join(settings.MEDIA_ROOT, 'queu')
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Created directory: {directory}")

        filepath = os.path.join(directory, filename)
        logger.info(f"Filepath for test file: {filepath}")

        # Create a simple text file
        with open(filepath, 'w') as f:
            f.write("This is a test file.")
        
        logger.info(f"Test file {filepath} created successfully")

        # Check if the file exists and log its size
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            logger.info(f"File {filepath} exists, size: {file_size} bytes")
        else:
            logger.error(f"File {filepath} does not exist")

        return filepath
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
    
    

@shared_task
def send_reminder_emails():
    
    today = timezone.now().date()
    two_days_ahead = today + timedelta(days=2)

    active_contracts = Fa_Contract.objects.filter(status=1).values_list('id', flat=True)

    # Subquery to get the latest `uploaded_at` for each contract
    latest_pm_subquery = PreventiveMaintenance.objects.filter(
        contract=OuterRef('contract')
    ).order_by('-uploaded_at').values('uploaded_at')[:1]
    
 

    # Filter for latest PM records and check if next_pm_date matches two_days_ahead
    latest_pms = PreventiveMaintenance.objects.filter(
        contract__in=active_contracts,
        uploaded_at=Subquery(latest_pm_subquery),
        next_pm_date=two_days_ahead
    ).select_related('contract', 'station_name', 'Created_By')
    
    count_upcoming_maintenances = latest_pms.count()
    
    if latest_pms.exists():
        # Send email notifications
        for pm in latest_pms:
            contract_id = pm.contract.contract_reference_number
            station_name = pm.station_name if pm.station_name else 'N/A'
            technician_email = 'ajmalummer30@gmail.com'  # Adjust as needed
            subject = f"Reminder: Scheduled Preventive Maintenance - Contract {contract_id}"
            message = (f"Dear Team,\n\n"
                       f"This is a reminder that you have a scheduled Preventive Maintenance "
                       f"for Contract {contract_id} at {station_name} on {pm.next_pm_date}.\n\n"
                       f"Please make necessary arrangements.\n\n"
                       f"Regards,\nYour Maintenance Team\n\n")
            
            send_mail(subject, message, 'noreply@sats.com.sa', [technician_email])
        
    # Check for overdue PMs (i.e., those whose next_pm_date is before today)
    overdue_pms = PreventiveMaintenance.objects.filter(
        contract__in=active_contracts,
        uploaded_at=Subquery(latest_pm_subquery),
        next_pm_date__lt=today
    ).select_related('contract', 'station_name', 'Created_By')
    
    count_overdue_maintenances = overdue_pms.count()
    
    if overdue_pms.exists():
            
        for pm in overdue_pms:
            contract_id = pm.contract.contract_reference_number
            station_name = pm.station_name if pm.station_name else 'N/A'
            technician_email = 'ajmalummer30@gmail.com'  # Adjust as needed
            subject = f"Scheduled Preventive Maintenance Overdue - Contract {contract_id}"
            message = (f"Dear Team,\n\n"
                    f"This is a reminder that the Preventive Maintenance "
                    f"for Contract {contract_id} at {station_name} was due on {pm.next_pm_date}.\n\n"
                    f"Please make necessary arrangements as soon as possible.\n\n"
                    f"Regards,\nYour Maintenance Team\n\n")
            
            send_mail(subject, message, 'noreply@sats.com.sa', [technician_email])
        

    return f"Found {count_upcoming_maintenances} upcoming preventive maintenances and {count_overdue_maintenances} overdue maintenance."

@shared_task
def send_reminder_emails_test():
    
    today = timezone.now().date()
    two_days_ahead = today + timedelta(days=2)

    active_contracts = Fa_Contract.objects.filter(status=1).values_list('id', flat=True)

    # Subquery to get the latest `uploaded_at` for each contract
    latest_pm_subquery = PreventiveMaintenance.objects.filter(
        contract=OuterRef('contract')
    ).order_by('-uploaded_at').values('uploaded_at')[:1]
    
 

    # Filter for latest PM records and check if next_pm_date matches two_days_ahead
    latest_pms = PreventiveMaintenance.objects.filter(
        contract__in=active_contracts,
        uploaded_at=Subquery(latest_pm_subquery),
        next_pm_date=two_days_ahead
    ).select_related('contract', 'station_name', 'Created_By')
    

    

    # Create an HTML table
    html_output = "<html><body>"
    html_output += "<h2>Upcoming Preventive Maintenances</h2>"
    html_output += "<table border='1'><thead><tr><th>Contract ID</th><th>Station Name</th><th>Created By</th><th>Uploaded At</th><th>Next PM Date</th></tr></thead><tbody>"

    # Loop through the result set and generate table rows
    for pm in latest_pms:
        contract_id = pm.contract.contract_reference_number
        station_name = pm.station_name if pm.station_name else 'N/A'
        created_by = pm.Created_By.username if pm.Created_By else 'N/A'
        uploaded_at = pm.uploaded_at
        next_pm_date = pm.next_pm_date

        html_output += f"<tr><td>{contract_id}</td><td>{station_name}</td><td>{created_by}</td><td>{uploaded_at}</td><td>{next_pm_date}</td></tr>"

    html_output += "</tbody></table>"
    html_output += "</body></html>"




    return f"Found  upcoming preventive maintenances."


@shared_task
def Send_Emails_Contract_Expiry():
    today = timezone.now().date()
    
    # Calculate dates for 20 days and 10 days before expiry
    twenty_days_ahead = today + timedelta(days=20)
    ten_days_ahead = today + timedelta(days=10)
    
  

    # Get contracts expiring in 20 days
    contracts_expiring_in_20_days = Fa_Contract.objects.filter(
        status=1,  # Only active contracts
        end_date=twenty_days_ahead
    )
    count_upcoming_maintenances_20 =contracts_expiring_in_20_days.count()
    
    # Get contracts expiring in 10 days
    contracts_expiring_in_10_days = Fa_Contract.objects.filter(
        status=1,  # Only active contracts
        end_date=ten_days_ahead
    )
    count_upcoming_maintenances_10 =contracts_expiring_in_10_days.count()
    
    
    # Send email for contracts expiring in 20 days
    for contract in contracts_expiring_in_20_days:
        send_contract_expiry_email(contract, 20)
    


    # Send email for contracts expiring in 10 days
    for contract in contracts_expiring_in_10_days:
        send_contract_expiry_email(contract, 10)
        
    

    return f"Contract expiry reminders sent for 10 days {count_upcoming_maintenances_10} and for 20 days {count_upcoming_maintenances_20}."

def send_contract_expiry_email(contract, days_before_expiry):
    # Contract details
    contract_id = contract.contract_reference_number
    station_name = contract.station_name if contract.station_name else 'N/A'
    end_date = contract.end_date
   
    # Email subject and message
    technician_email = 'ajmalummer30@gmail.com'  # Adjust as needed
    subject = f"Reminder: Contract {contract_id} is expiring in {days_before_expiry} days"
    message = (f"Dear Team,\n\n"
               f"This is a reminder that the contract {contract_id} at {station_name} is set to expire on {end_date}.\n\n"
               f"Please note: If the contract has already been renewed, kindly ignore this message.\n\n"
               f"Regards,\nYour Contract Management Team\n\n")
    
    # Send the email
    send_mail(subject, message, 'noreply@sats.com.sa', [technician_email])


        