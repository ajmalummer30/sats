
from django.contrib import admin
from django.urls import include, path
from accounts.serializers import LoginView
from accounts.views import *
from django.contrib.auth import views as auth_views

app_name='accounts' 




urlpatterns = [
    path('', home , name='home' ),
    path('journey/', journey , name='journey' ),
    path('contact/', contact , name='contact' ),
    path('network/', network , name='network' ),
    path('signup/', sign_up, name='signup'),
    path('logout/',sign_out, name='logout'),
    #path('', sign_in, name='login'),
     path('login/', sign_in, name='login'),
    #path('login/', auth_views.LoginView.as_view(),name='login'),
    path('api/login/', LoginView.as_view(), name='loginView'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
    
    
   
    
   
    
]