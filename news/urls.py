from django.urls import include, path
from itassets.views import *
from . import views
app_name= 'news'


urlpatterns = [
    path('getpost/', views.get_post , name='get_post' ),
    path('getpost/<id>', views.get_post_id , name='get_post_id' ),
    
]