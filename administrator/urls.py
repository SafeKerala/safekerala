
from django.urls import path
from .views import *

urlpatterns = [
    path('admindashboard',admindashboard.as_view(),name='admindashboard'),
    path('viewcomplaints',viewcomplaints.as_view(),name='viewcomplaints'),
    path('viewlabours',viewlabours.as_view(),name='viewlabours'),
    path('viewpolicestation',viewpolicestation.as_view(),name='viewpolicestation'),
    path('sendnotification',sendnotification.as_view(),name='sendnotification'),
    path('viewfeedback',viewfeedback.as_view(),name='viewfeedback'),
    path('replycomplaint',replycomplaint.as_view(),name='replycomplaint'),
    path('policestationdashboard',policestationdashboard.as_view(),name='policestationdashboard'),
    path('criminallistmanagement',criminallistmanagement.as_view(),name='criminallistmanagement'),
    path('sendsolution',sendsolution.as_view(),name='sendsolution'),
     path('userdashboard',userdashboard.as_view(),name='userdashboard'),
    path('addcomplaint',addcomplaint.as_view(),name='addcomplaint'),
    path('sendfeedback',sendfeedback.as_view(),name='sendfeedback'),
    path('sendrequestforlabours',sendrequestforlabours.as_view(),name='sendrequestforlabours'),
    path('viewrequeststatus',viewrequeststatus.as_view(),name='viewrequeststatus'),


    
path('editcriminals',editcriminals.as_view(),name='editcriminals'),
    path('editlabours',editlabours.as_view(),name='editlabours'),
]

