"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from websockets.views import text_to_speech


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('websocket/', include('websockets.urls')),
    path('', include('accounts.urls')),
    path('news/', include('news.urls')),
    path('usrmgmt/', include('user_management.urls')),
    path('polls/', include('polls.urls')),
    path('pettycash/', include('pettycash.urls')),
    path('itassets/', include('itassets.urls')),
    path('safety/', include('quality.urls')),
    path('tts/', text_to_speech, name='text_to_speech'),
]
