from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.db import connection
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

myCursor = connection.cursor()

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        email = request.POST['email']
        mob = request.POST['mob']
        utype = request.POST['utype']

        u = User(first_name = fname,last_name = lname,username = uname, password = make_password(pwd), email = email)
        u.save()

        up = UserProfile(user=u,mobile= mob,usertype = utype)
        up.save()
        return redirect('/signup/')

    return render(request,'signup.html')

def login_call(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        selectedUser = authenticate(username = uname,password = pwd) 
        if selectedUser:
            login(request,selectedUser)
            uObj = UserProfile.objects.get(user__username=request.user)
            #print(request.user)
            #"select usertype from ecommerceproject_userprofile where user_id=(select id from auth_user where username = 'alka123')
            if uObj.usertype == 'buyer':
                return redirect('/buyer/home/')
            elif uObj.usertype == 'seller':
                return redirect('/seller/home/')
        else:
            return HttpResponse("<h1>Wrong Credentials!</h1>")

    return render(request,"login.html")

def logout_call(request):
    logout(request)
    return redirect('/login/')