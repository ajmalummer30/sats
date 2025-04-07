from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
import django
django.setup()
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.

app = Celery('myproject')
#app.conf.broker_connection_retry_on_startup = True

# Using Redis as the broker
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.timezone = 'Asia/Riyadh'

app.conf.beat_schedule = {
    'send-PMoverdue-reminder-emails-every-day': {
        'task': 'myproject.tasks.send_reminder_emails',
        'schedule': crontab(hour=23, minute=15),  # Schedule to run every day at 7:30 AM
    },
    # New task: subtract every day
    'test-every-day': {
        'task': 'myproject.tasks.send_reminder_emails_test',  # Make sure to adjust the path as needed
        'schedule': crontab(hour=22, minute=15),  # Schedule this to run at 7:00 PM every day
    },
    # New task: subtract every day
    'send-contract-expiry-notification': {
        'task': 'myproject.tasks.Send_Emails_Contract_Expiry',  # Make sure to adjust the path as needed
        'schedule': crontab(hour=11, minute=30),  # Schedule this to run at 7:00 PM every day
    },
    
    

    
}

