from django.urls import re_path
from django.urls import path
from . import consumers

websocket_urlpatterns = [
   
   re_path(r'ws/queue/$', consumers.QueueConsumer.as_asgi()),
]