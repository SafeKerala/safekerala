from django.shortcuts import render
from django.views import View

# Create your views here.
class admindashboard(View):
    def get(self,request)
        return render(request,'admin/admindashboard.html')
class viewcomplaints(View):
    def get(self,request)
        return render(request,'admin/viewcomplaints.html')
class viewcriminal(View):
    def get(self,request)
        return render(request,'admin/viewcriminals.html')  
class viewlabours(View):
    def get(self,request)
        return render(request,'admin/viewlabours.html')
class viewpolicestation(View):
    def get(self,request)
        return render(request,'admin/viewpolicestation.html') 
class login(View):
    def get(self,request)
        return render(request,'admin/login.html')
class editcriminals(View):
    def get(self,request)
        return render(request,'editcriminals.html')       
class editlabours(View):
    def get(self,request)
        return render(request,'editlabours.html') 
class policestationdashboard(View):
    def get(self,request)
        return render(request,'policestationdashboard.html') 
class register(View):
    def get(self,request)
        return render(request,'register.html')                                     
class replycomplaint(View):
    def get(self,request)
        return render(request,'replycomplaint.html') 
class sendnotification(View):
    def get(self,request)
        return render(request,'sendnotification.html')
class sendsolution(View):
    def get(self,request)
        return render(request,'sendsolution.html')
 class viewfeedback(View):
    def get(self,request)
        return render(request,'viewfeedback.html')        
               

                

