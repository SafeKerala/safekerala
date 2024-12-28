from django.shortcuts import render
from django.views import View

# Create your views here.
class admindashboard(View):
    def get(self,request):
        return render(request,'admin/admindashboard.html')
class viewcomplaints(View):
    def get(self,request):
        return render(request,'admin/viewcomplaints.html')
class viewlabours(View):
    def get(self,request):
        return render(request,'admin/viewlabours.html')
class viewpolicestation(View):
    def get(self,request):
        return render(request,'admin/viewpolicestation.html') 
class sendnotification(View):
    def get(self,request):
        return render(request,'admin/sendnotification.html') 
class viewfeedback(View):
    def get(self,request):
        return render(request,'admin/viewfeedback.html')
class replycomplaint(View):
    def get(self,request):
        return render(request,'admin/replycomplaint.html')
class policestationdashboard(View):
    def get(self,request):
        return render(request,'police/policestationdashboard.html')            
class criminallistmanagement(View):
    def get(self,request):
        return render(request,'police/criminallistmanagement.html') 
class sendsolution(View):
    def get(self,request):
        return render(request,'police/sendsolution.html')
class userdashboard(View):
    def get(self,request):
        return render(request,'user/userdashboard.html')        
class addcomplaint(View):
    def get(self,request):
        return render(request,'user/addcomplaint.html')        
class sendfeedback(View):
    def get(self,request):
        return render(request,'user/sendfeedback.html')        
class sendrequestforlabours(View):
    def get(self,request):
        return render(request,'user/sendrequestforlabours.html')                
class viewrequeststatus(View):
    def get(self,request):
        return render(request,'user/viewrequeststatus.html')        








class editcriminals(View):
    def get(self,request):
        return render(request,'editcriminals.html')       
class editlabours(View):
    def get(self,request):
        return render(request,'editlabours.html')                                   

               

                

