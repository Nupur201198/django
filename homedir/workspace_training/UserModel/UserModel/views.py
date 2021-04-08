from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

def signup(request):
    uf = UserForm()
    if request.method == 'POST':
        uf2 = UserForm(request.POST)
        if uf2.is_valid():
            ufsaved = uf2.save()
            ufsaved.set_password(ufsaved.password)
            ufsaved.save()

    return render(request, 'signup.html',{'data': uf})

def login_call(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        selectedUser = authenticate(username = uname, password = pwd)
        if selectedUser:
            login(request,selectedUser)
            print(selectedUser)
            return redirect('/welcome/')
        else:
            return HttpResponse("<h1>Wrong Credentials</h1>")
    else:
        return render(request,'login.html')

def logout_call(request):
    logout(request)
    return redirect('/login/')

def welcome(request):
    return render(request,'welcome.html')