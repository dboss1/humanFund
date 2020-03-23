from django.shortcuts import render, redirect

from .models import User
from .forms import RegisForm,Login,Portal


def registration(request):
    if request.method == 'POST':
        regisForm = RegisForm(request.POST)
        
        if form.is_valid():
            new_registration = User(username=request.POST['username'],
                password=request.POST['password'],
                fName=request.POST['fName'],
                mName=request.POST['mName'],
                lName=request.POST['lName'],
                gender=request.POST['gender'],
                address=request.POST['address'],
                city=request.POST['city'],
                email=request.POST['email'],
                cellPhone=request.POST['cellPhone'],
                country=request.POST['country'],
                dob=request.POST['dob'])
            new_registration.save()
            return redirect('humanFund')
        
    else:
        regisForm = RegisForm()
    
    context = {'regisForm' : regisForm}
    return render(request, 'registration/registration.html',{'regisForm': regisForm})

def humanFund(request):
   
    return render(request, 'registration/humanFund.html')
    
def portal(request):
    portal = Portal()
    return render(request, 'registration/portal.html', {'portal' : portal})

def login(request):
    login = Login()
    
    context = {'login' : login}
    return render(request, 'registration/login.html',{'login': login})

