from django.contrib import admin
from django.urls import include, path
from myproject.tasks import send_reminder_emails, send_reminder_emails_test
from polls.views import *
from . import views
app_name= 'polls'


urlpatterns = [
    path('', home , name='home' ),
    path('facilities/', facility_menu , name='facility_menu' ),
    path('get_questions/', get_questions , name='get_questions' ),
    path('display_checklist/', display_checklist , name='display_checklist' ),
    path('detail_view/<id>', detail_view , name='detail_view' ),
    path('generate_invoice/<id>',generate_invoice , name='generate_invoice' ),
    path('createquestions/', create_questions , name='create_questions' ),
    path('create_Dieselquestions/', create_Dieselquestions , name='create_Dieselquestions' ),
    path('UpdateQuestions/<id>',UpdateQuestions , name='UpdateQuestions' ),
    path('DeleteQuestions/<id>',DeleteQuestions , name='DeleteQuestions' ),
    path('createworkpermit/', CreateWorkpermitView , name='createworkpermit' ),
    path('displayworkpermits/', WorkpermitsDisplayView , name='displayworkpermits' ),
    path('Editworkpermit/<id>', Editworkpermit , name='Editworkpermit' ),
    path('detailwpview/<id>', DetailWorkpermitsView , name='detailwpview' ),
    path('wppdfgenerate/<id>', wppdfgenerate , name='wppdfgenerate' ),
    path('import_data_to_db/', import_data_to_db),
    path('simple_upload/', simple_upload, name='simple_upload'),
    path('incidentform/', incident_form, name='incident_form'),
    path('gatepass/', Gatepass, name='gatepass'),
    path('gatepassadditems/<id>', GatePassAddItems, name='gatepassadditems'),
    path('displaygatepass/', Display_GatePass, name='display_gatepass'),
    path('DetailViewGatepass/<id>', Detail_gatepassView, name='DetailViewGatepass'),
    path('DetailViewGatepassPdf/<id>', Detail_gatepassViewPdf, name='DetailViewGatepassPdf'),
    path('UpdateReturndateAjax/', update_return_dateAjax , name='UpdateReturnDateAjax' ),
    path('saveworkerinfo/', SaveWorkerinfo , name='saveworkerinfo' ),
    path('savecompanyinfo/', SaveCompanyinfo , name='savecompanyinfo' ),
    path('displayworkermodal/', Ajax_ShowWorkerModal , name='DisplayWorkerModal' ),
    path('displaycompanymodal/', Ajax_ShowCompanyModal , name='DisplayCompanyModal' ),
    path('addcategory/', add_category , name='add_category' ),
    path('faaddcontracts/', add_Fa_contracts , name='add_Fa_contracts' ),
    path('faviewcontracts/', ContractsView , name='ContractsView' ),
    path('faaddsubcategory/', add_sub_category , name='add_sub_category' ),
    path('viewcategories/', View_category , name='View_category' ),
    path('get_subcategories/<int:category_id>/', get_subcategories, name='getsubcategories'),
    path('get-contract-details/', get_contract_details, name='get_contract_details'),
    path('detailcontractsview/<id>', DetailContractsView , name='DetailContractsView' ),
    path('addvendor/', Add_Vendor, name='Add_Vendor'),
    path('issuepm/', IssuePM , name='IssuePM' ),
    path('issuecm/', IssueCM , name='IssueCM' ),
    path('issuenewwork/', issue_new_maintenance , name='issuenewwork' ),
    path('pmview/', PMView , name='PMView' ),
    path('cmview/', CMView , name='CMView' ),
    path('uploadpmfiles/', uploadpmfiles , name='uploadpmfiles' ),
    path('uploadcmfiles/', uploadcmfiles , name='uploadcmfiles' ),
    path('uploadnewfiles/', uploadnewfiles , name='uploadnewfiles' ),
     path('uploadnewfileshtmx/', uploadnewfiles_htmx , name='uploadnewfiles_htmx' ),
    path('addpmcomment/', add_comment, name='add_comment'),
    path('addcmcomment/', add_CM_comment, name='add_CM_comment'),
    path('addnewworkcomment/', add_Newwork_comment, name='AddNewWorkComment'),
    path('addnewworkcommenthtmx/', add_NewWork_comment_htmx, name='add_NewWork_comment_htmx'),
    path('workorderview/', WorkOrderView , name='WorkOrderView' ),
    path('createwpnew/<id>', Create_WorkPermit_NewWork, name='createwpnew'),
    path('createwppm/<id>', Create_WorkPermit_PM, name='Create_WorkPermit_PM'),
    #path('createwpcm/<id>', Create_WorkPermit_CM, name='Create_WorkPermit_CM'),
    path('createwpcm/<int:id>/', Create_WorkPermit_CM, name='Create_WorkPermit_CM'),
    path('detailworkorderview/<id>', Detail_Work_Order_View, name='Detail_Work_Order_View'),
    path('events/', calendar_events, name='calendar-events'),
    path('displayevents/', displayevents, name='displayevents'),
    path('sendemail/', send_reminder_emails_test , name='sendemail' ),
        path('filterworkpermits/', filter_petty_workpermits , name='filter_petty_workpermits' ),
    
      
    
]