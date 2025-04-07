from django.urls import include, path
from itassets.views import *
from . import views
app_name= 'itassets'


urlpatterns = [
     path('productupload/', It_Product_Upload, name='It_Product_Upload'),
     path('ItProductAdd/', It_Product_Add, name='It_Product_Add'),
     path('itassetdisplay/', itassetdisplay, name='itassetdisplay'),
     path('itassetdetailview/<id>', ItAssetDetailView, name='ItAssetDetailView'),
     path('itassethistory/<int:id>/', view_asset_db_history, name='itasset_history'),
     path('itassetfilter/', itassetfilter, name='itassetfilter'),
     path('EditItAsset/<id>', EditItAsset, name='EditItAsset'),
     path('AllocateAssetIT/<id>',allocate_asset_view, name='Allocate_Asset_IT'),
     path('', It_Graph_Display, name='It_Graph_Display'),
     path('getasset/', get_serial_asset, name='getasset'),
     path('getuser/', get_user_details, name='getuser'),
     path('assetallocation/', allocate_it_asset, name='allocate_it_asset'),
     path('deallocateasset/<id>', test_deallocate_asset, name='test_deallocate_asset'),
     path('htmltopdf/<id>', htmltopdf, name='htmltopdf'),
     path('choicesview/', choices_view, name='choices_view'),
     path('itModalAjaxautocomplete/', ItModal_Ajaxautocomplete, name='itModalAjaxautocomplete'),
     path('saveitbrand/', Save_ItBrand, name='SaveItBrand'),
     path('saveitcategory/', Save_ItCategory, name='SaveitCategory'),
     path('displayajaxitcategory/', Ajax_display_ItBrand, name='DisplayItBrand'),
     path('displayajaxitcategory/', Ajax_display_ItCategory, name='DisplayItCategory'),
     path('getbrandcategory/', get_brand_and_category, name='GetBrandCategory'),
     path('displayitmodal/', Ajax_display_ItModel, name='AjaxdisplayItModel'),
     path('saveitmodal/', Ajax_Save_ItModel, name='AjaxsaveItModel'),
     path('createmaintanencerequest/', create_maintenance_request, name='create_main_request'),
     path('createmaintanencerequest/<id>', create_maintenance_requestid, name='create_main_request_id'),
     path('editmaintanencerequest/<id>', Edit_maintenance_requestid, name='Edit_maintenance_request_id'),
     path('viewmaintupdatehistory/', Maint_update_history_view, name='Maint_update_history'),
     #path('multiform/', FormWizardView.as_view(), name='multiform'),
     #path('itproductcreate/', ItProductsWizardView.as_view(), name='itproductcreate'),
     path('itproductupdate/<int:pk>/', ItProductsWizardUpdateView.as_view(), name='itproductupdate'),
     #path('allocateitasset/<id>', allocate_asset_test, name='allocateitasset'),
     #path('Assetaddtest/', assetaddtest, name='Assetaddtest'),
     path('test/', assetllocationtest, name='test'),
     
    
    
]
