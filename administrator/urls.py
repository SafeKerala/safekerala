
from django.urls import path
from .views import *

urlpatterns = [
    path('admindashboard',admindashboard.as_view(),name='admindashboard'),
    path('viewcomplaints',viewcomplaints.as_view(),name='viewcomplaints'),
    path('viewcriminal',viewcriminals.as_view(),name='viewcriminals'),
    path('viewlabours',viewlabours.as_view(),name='viewlabours'),
    path('viewpolicestation',viewpolicestation.as_view(),name='viewpolicestation'),
    path('login',login.as_view(),name='login'),
    path('editcriminals',editcriminals.as_view(),name='editcriminals'),
    path('editlabours',editlabours.as_view(),name='editlabours'),
    path('policestationdashboard',policestationdashboard.as_view(),name='policestationdashboard'),
    path('register',register.as_view(),name='register'),
    path('replycomplaint',replycomplaint.as_view(),name='replycomplaint'),
    path('sendnotification',sendnotification.as_view(),name='sendnotification'),
    path('sendsolution',sendsolution.as_view(),name='sendsolution'),
    path('viewfeedback',viewfeedback.as_view(),name='viewfeedback'),
    
    

]

