from django.shortcuts import render,redirect
from django.contrib import messages
from Nitclinic.forms import patientform,userform
from Nitclinic.models import patient,user_login
# Create your views here.
def home(request):
    return render(request,'home.html')
def inscode(request):
    if request.method=="POST":
        dt=userform(request.POST)
        if dt.is_valid():
            dt.save()
            return render(request,'index.html')
        else:
            dt=userform()
            return render(request,'sign.html')
def sig(request):
    return render(request,'sign.html')       

def insert(request):
    return render(request,'appointment.html')   
def inpcode(request):
    if request.method=="POST":
        de=patientform(request.POST)
        if de.is_valid():
            de.save()
            messages.success(request,'your form is submitted')
            return render(request,'appointment.html')
        else:
            messages.error(request,'form is invalid')
            messages.error(request,de.errors)
    else:    
        de=patientform()
        return render(request,'appointment.html')
def login(request):
    return render(request,'index.html')
def log(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        try:
            t=user_login.objects.get(email=email)
            c=user_login.objects.get(password=password)
            if t and c is not None :
                return render(request,'appointment.html') 
            else:
                return render(request,'index.html')
        except:
             return render(request,'index.html')
def about(request):
            return render(request,'about.html')
