from django.contrib import admin
from django.urls import path
from pettycash.views import *
from .views import (
    ProductList, ProductCreate, ProductUpdate,delete_variant
    
)

app_name= 'pettycash'


urlpatterns = [
    
    path('home/', home , name='home' ),
    path('travelclaim/', TravelClaimcreate , name='travelclaim' ),
    path('travelclaimrequest/', Travelclaimrequest , name='travelclaimrequest' ),
    #path('', expense_form , name='expenseitem' ),
    #path('products/', ProductList.as_view(), name='list_products'),
    path('products/', displayclaims, name='list_products'),
    path('listuserclaims/', ViewUserTravelClaims, name='ViewUserTravelClaims'),
    path('listuserpettycash/', ViewUserPettyCash, name='ViewUserPettyCash'),
    path('listalluserpettycash/', ViewAllUserPettyCash, name='ViewAllUserPettyCash'),
    path('DetailViewuserpc/<int:id>/', ViewUserPettyCashDetail, name='ViewUserPettyCashDetail'),
    path('TcManagerView/', Tc_Manager_View, name='Tc_Manager_View'),
    path('PcManagerView/', Pc_Manager_View, name='Pc_Manager_View'),
    path('create/', ProductCreate.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='update_product'),
    path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),
    path('Mgrtcapprove/<int:id>/', MgrEmailclaimView, name='MgrEmailclaimView'),
    #path('Mgrpcapprove/<int:id>/', MgrEmailclaimView, name='MgrEmailclaimView'),
    #path('handle_approval/<int:claim_id>/<str:action>/<str:token>/', handle_approval, name='handle_approval'),
    path('handle_approval/<int:claim_id>/<str:action>/', handle_approval, name='handle_approval'),
    path('ApproveTcClaim/<int:id>/<str:action>/', ApproveTravelClaim, name='ApproveTcClaim'),
    path('ApprovePcClaim/<int:id>/<str:action>/', ApprovePettyCash, name='ApprovePcClaim'),
    path('downloadpdftc/<int:id>/', travelclaimpdfdownload, name='travelclaimpdf'),
    path('downloadpdfpt/<int:id>/', pettycashpdfdownload, name='pettycashpdf'),
    path('filter_petty_requests/', filter_petty_requests, name='filter_petty_requests'),
]
      
    
