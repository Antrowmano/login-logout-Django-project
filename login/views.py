from django.shortcuts import render
from django.contrib import messages
from login.models import Newuser

# Create your views here.

def index(request):
    return render(request,'index.html')


def registration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        Email=request.POST['Email']
        Pwd=request.POST['Pwd']
        Age=request.POST['Age']
        Gender=request.POST['Gender']
        MartialStatus=request.POST['MartialStatus']
        Newuser(Username=Username,Email=Email,Pwd=Pwd,Age=Age,Gender=Gender,MartialStatus=MartialStatus).save()
        messages.success(request,'The New User'+request.POST['Username']+"Is Saved Successfully....!")
        return render(request,'registration.html')
    
    else:
         return render(request,'registration.html')

def login(request):
    if request.method == 'POST':
        try:
            Userdetails=Newuser.objects.get(Email=request.POST['Email'],Pwd=request.POST['Pwd'])
            print("Username=",Userdetails)
            request.session['Email']=Userdetails.Email
            return render(request,'Index.html')
        except Newuser.DoesNotExist as e :
            messages.success(request,'Username / password Invalid...!')
    return render(request,'login.html')

