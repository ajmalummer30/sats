from django.urls import path
from . import views

app_name= 'websockets'

urlpatterns = [
  
    path('staff/', views.staff_view, name='staff'),
    path('', views.display_view, name='display'),
    #path('generate_announcement/<int:token_number>/<int:counter_number>/', views.generate_announcement, name='generate_announcement'),
    path('issue_ticket/', views.issue_ticket_view, name='issue_ticket'),
    path('opentickets/', views.get_open_tickets, name='get_open_tickets'),
    path('last_ticket_number/', views.get_last_ticket_number, name='last_ticket_number'),
    
    
]