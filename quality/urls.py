from django.contrib import admin
from django.urls import include, path
from quality.views import *
from . import views
from .views import EmployeeDetailView,EmployeeCreateView
from rest_framework.routers import DefaultRouter


app_name= 'quality'

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)  # Registers the viewset
router.register(r'drivers', DriverViewSet)
router.register(r'country', CountryViewSet)
router.register(r'states', StatesViewSet)
from rest_framework.authtoken import views as drf_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




customurlpatterns = [ 
              path('', home , name='home' ), 
              path('mouseentered/', mouse_entered , name='mouse_entered' ),
              path('usernamecheck/', username , name='username' ),
              path('test-api/', views.test_get_and_post_api, name='test_api'),
              path('test-api-jwt/', views.test_get_and_post_api_jwt, name='test_api'),
              path('sendnotification/', send_notification , name='send_notification' ),
              path('SaveDriverinfo/', SaveDriverinfo , name='savedriverinfo' ),
              path('listincidents/', listincidents , name='listincidents' ),
              path('incidentdetailview/<id>', incidentdetailview, name='incidentdetailview'),
             # path('employeecreate/', EmployeeCreateView.as_view(), name='EmployeeCreateView'),
              #path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='EmployeeDetailView'),
              path('api-token-auth/', drf_views.obtain_auth_token, name='api_token_auth'),
              path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT
              path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT
  
               ]

urlpatterns = customurlpatterns + router.urls 